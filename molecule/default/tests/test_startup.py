import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_influx_service_enabled(host):
    """Test InfluxDB service enabled

    """
    service = host.service('influxdb')
    assert service.is_enabled


def test_influxdb_running(host):
    """Test that influxdb is running
    """
    service = host.service('influxdb')
    assert service.is_running


def test_influxdb_listening_on_port(host):
    """Test that influxdb is listening on port
    """
    assert host.socket("tcp://0.0.0.0:8086").is_listening
