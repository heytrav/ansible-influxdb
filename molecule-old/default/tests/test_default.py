import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/influxdb/influxdb.conf')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_config_logging_enabled(host):
    """Test whether shard precreation is true

    :host: host object
    """
    content = host.file('/etc/influxdb/influxdb.conf').content_string
    meta_logging_enabled_pattern = re.compile(
            r"^\s+logging-enabled\s+=\s+(?P<logging_enabled>[^\s]+)\s*$", re.M
            | re.X)
    trace_logging_enabled_pattern = re.compile(
            r"""^\s+
            trace-logging-enabled
            \s+=\s+
            (?P<logging_enabled>[^\s]+)
            \s*$""",
            re.M | re.X)

    meta_result = re.search(meta_logging_enabled_pattern, content)
    trace_result = re.search(trace_logging_enabled_pattern, content)
    assert meta_result.group('logging_enabled') in ['true', 'false']
    assert trace_result.group('logging_enabled') in ['true', 'false']


def test_config_boolean_case_correct(host):
    """Make sure config does not contain incorrect jinja booleans

    :host: host object

    """
    file = host.file('/etc/influxdb/influxdb.conf')
    assert not file.contains('= True')
    assert not file.contains('= False')


def test_database_directory_created(host):
    """Test that install sets up database directory

    :host: host object

    """
    assert host.file('/var/lib/influxdb').is_directory
