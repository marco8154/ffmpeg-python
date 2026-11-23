import pytest

import ffmpeg
from ffmpeg.dag import DagEdge, topo_sort


def chain(n):
    s = ffmpeg.input('in.mp4')
    for i in range(n):
        s = s.filter('hue', s=i % 10)
    return s.output('out.mp4')


def test_chain_2000_filters():
    args = chain(2000).get_args()
    filter_arg = args[args.index('-filter_complex') + 1]
    assert filter_arg.count('hue=') == 2000


class _CyclicNode(ffmpeg.dag.DagNode):
    """Minimal node mock with a controllable set of incoming edges."""

    def __init__(self, name):
        self.name = name
        self.edges = []

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, _CyclicNode) and self.name == other.name

    @property
    def incoming_edges(self):
        return list(self.edges)


def test_cycle_still_detected():
    node_a = _CyclicNode('a')
    node_b = _CyclicNode('b')
    node_a.edges.append(DagEdge(node_a, 'in', node_b, 'out', None))
    node_b.edges.append(DagEdge(node_b, 'in', node_a, 'out', None))
    with pytest.raises(RuntimeError, match='Graph is not a DAG'):
        topo_sort([node_a])
