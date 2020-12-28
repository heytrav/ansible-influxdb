ansible-influxdb
=========

[![Build Status](https://travis-ci.com/heytrav/ansible-influxdb.svg?branch=master)](https://travis-ci.com/heytrav/ansible-influxdb)

Install InfluxDB on a host


Requirements
------------

No special requirements.

Role Variables
--------------


| Variable  | Default | Description |
| ---  | --- | --- |
| influxdb_url | | Source url for influxdb package. Depends on OS (Centos or Ubuntu) |
|influxdb_version| 2.0.3 | InfluxDB version | 
| influxdb_admin_user | admin | Name of the admin user |
| influxdb_admin_user_password | _not defined_ | Define this if you want to create an admin user. Default behaviour is to not create an admin user.| 
| influxdb_admin_organization | admin | Organisation name of admin user |
| influxdb_primary_bucket | "primary" | |
| influxdb_retention_period | `24 * 180` | Retention period in hours. Defaults to 180 days |

See the [InfluxDB documentation](https://docs.influxdata.com/influxdb/v2.0/reference/config-options/) for a description of configuration options. This role assumes the official documented default values for all configuration options. The following variables can be used to override the InfluxDB default values:

* `influxdb_assets_path`
* `influxdb_bolt_path`
* `influxdb_e2e_testing`
* `influxdb_engine_path`
* `influxdb_http_bind_address`
* `influxdb_influxql_max_select_buckets`
* `influxdb_influxql_max_select_point`
* `influxdb_influxql_max_select_series`
* `influxdb_log_level`
* `influxdb_new_meta_store`
* `influxdb_new_meta_store_read_only`
* `influxdb_no_tasks`
* `influxdb_query_concurrency`
* `influxdb_query_initial_memory_bytes`
* `influxdb_query_max_memory_bytes`
* `influxdb_query_memory_bytes`
* `influxdb_query_queue_size`
* `influxdb_reporting_disabled`
* `influxdb_secret_store`
* `influxdb_session_length`
* `influxdb_session_renew_disabled`
* `influxdb_storage_cache_max_memory_size`
* `influxdb_storage_cache_max_memory_size`
* `influxdb_storage_cache_snapshot_write_cold_duration`
* `influxdb_storage_compact_full_write_cold_duration`
* `influxdb_storage_compact_throughput_burst`
* `influxdb_storage_max_concurrent_compactions`
* `influxdb_storage_max_index_log_file_size`
* `influxdb_storage_retention_check_interval`
* `influxdb_storage_series_file_max_concurrent_snapshot_compactions`
* `influxdb_storage_series_id_set_cache_size`
* `influxdb_storage_shard_precreator_advance_period`
* `influxdb_storage_shard_precreator_check_interval`
* `influxdb_storage_tsm_use_madv_willneed`
* `influxdb_storage_validate_keys`
* `influxdb_storage_wal_fsync_delay`
* `influxdb_store`
* `influxdb_tls_cert`
* `influxdb_tls_key`
* `influxdb_tls_min_version`
* `influxdb_tls_strict_ciphers`
* `influxdb_tracing_type`
* `influxdb_vault_addr`
* `influxdb_vault_cacert`
* `influxdb_vault_capath`
* `influxdb_vault_client_cert`
* `influxdb_vault_client_key`
* `influxdb_vault_max_retries`
* `influxdb_vault_client_timeout`
* `influxdb_vault_skip_verify`
* `influxdb_vault_tls_server_name`
* `influxdb_vault_token`



Dependencies
------------

No external dependencies

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
        - role: heytrav.influxdb
          influxdb_admin_user_password: "{{ vault_influxdb_admin_user_password }}"


License
-------

BSD

Author Information
------------------

travis@catalyst
