from ffmpeg.dag import DagNode
import pytest


class _BareNode(DagNode):
    pass


def test_bare_node_repr_not_implemented():
    with pytest.raises(NotImplementedError):
        repr(_BareNode())
