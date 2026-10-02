from unittest.mock import patch
from freecad_mcp import server


def test_connection_uses_dedicated_port():
    old = server.state.freecad_connection, server.state.rpc_port
    try:
        server.state.freecad_connection = None
        server.state.rpc_port = 19875
        with patch.object(server, "FreeCADConnection") as connection:
            connection.return_value.ping.return_value = True
            server.get_freecad_connection()
            connection.assert_called_once_with(host=server.state.rpc_host, port=19875)
    finally:
        server.state.freecad_connection, server.state.rpc_port = old
