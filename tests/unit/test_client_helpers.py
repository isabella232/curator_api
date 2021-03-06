"""Test utility functions"""
# pylint: disable=C0103,C0111
from datetime import datetime, timedelta
from unittest import TestCase
from mock import Mock
import elasticsearch
from curator_api.helpers.client import get_version
from . import testvars as testvars

class TestGetVersion(TestCase):
    def test_positive(self):
        client = Mock()
        tupleversion = (9, 9, 9)
        for version in ['9.9.9', '9.9.9.dev', '9.9.9-dev']:
            client.info.return_value = {'version': {'number': version}}
            self.assertEqual(tupleversion, get_version(client))
    def test_negative(self):
        client = Mock()
        client.info.return_value = {'version': {'number': '9.9.9'}}
        version = get_version(client)
        self.assertNotEqual(version, (8, 8, 8))

# class TestIsMasterNode(TestCase):
#     def test_positive(self):
#         client = Mock()
#         client.nodes.info.return_value = {
#             'nodes': { "foo" : "bar"}
#         }
#         client.cluster.state.return_value = {
#             "master_node" : "foo"
#         }
#         self.assertTrue(curator.is_master_node(client))
#     def test_negative(self):
#         client = Mock()
#         client.nodes.info.return_value = {
#             'nodes': { "bad" : "mojo"}
#         }
#         client.cluster.state.return_value = {
#             "master_node" : "foo"
#         }
#         self.assertFalse(curator.is_master_node(client))




# class TestChunkIndexList(TestCase):
#     def test_big_list(self):
#         big = "superlongindexnamebyanystandardyouchoosethisissillyhowbigcanthisgetbeforeitbreaks"
#         indices = []
#         for i in range(100,150):
#             indices.append(big + str(i))
#         self.assertEqual(2, len(curator.chunk_index_list(indices)))
#     def test_small_list(self):
#         self.assertEqual(1, len(curator.chunk_index_list(['short','list','of','indices'])))

# class TestGetIndices(TestCase):
#     def test_client_exception(self):
#         client = Mock()
#         client.info.return_value = {'version': {'number': '5.0.0'} }
#         client.indices.get_settings.return_value = testvars.settings_two
#         client.indices.get_settings.side_effect = testvars.fake_fail
#         self.assertRaises(
#             curator.FailedExecution, curator.get_indices, client)
#     def test_positive(self):
#         client = Mock()
#         client.indices.get_settings.return_value = testvars.settings_two
#         client.info.return_value = {'version': {'number': '5.0.0'} }
#         self.assertEqual(
#             ['index-2016.03.03', 'index-2016.03.04'],
#             sorted(curator.get_indices(client))
#         )
#     def test_empty(self):
#         client = Mock()
#         client.info.return_value = {'version': {'number': '5.0.0'} }
#         client.indices.get_settings.return_value = {}
#         self.assertEqual([], curator.get_indices(client))

# class TestCheckVersion(TestCase):
#     def test_check_version_(self):
#         client = Mock()
#         client.info.return_value = {'version': {'number': '5.0.2'} }
#         self.assertIsNone(curator.check_version(client))
#     def test_check_version_less_than(self):
#         client = Mock()
#         client.info.return_value = {'version': {'number': '2.4.3'} }
#         self.assertRaises(curator.CuratorException, curator.check_version, client)
#     def test_check_version_greater_than(self):
#         client = Mock()
#         client.info.return_value = {'version': {'number': '7.0.1'} }
#         self.assertRaises(curator.CuratorException, curator.check_version, client)

# class TestCheckMaster(TestCase):
#     def test_check_master_positive(self):
#         client = Mock()
#         client.nodes.info.return_value = {
#             'nodes': { "foo" : "bar"}
#         }
#         client.cluster.state.return_value = {
#             "master_node" : "foo"
#         }
#         self.assertIsNone(curator.check_master(client, master_only=True))
#     def test_check_master_negative(self):
#         client = Mock()
#         client.nodes.info.return_value = {
#             'nodes': { "bad" : "mojo"}
#         }
#         client.cluster.state.return_value = {
#             "master_node" : "foo"
#         }
#         with self.assertRaises(SystemExit) as cm:
#             curator.check_master(client, master_only=True)
#         self.assertEqual(cm.exception.code, 0)

# class TestGetClient(TestCase):
#     # These unit test cases can't really get a client object, so it's more for
#     # code coverage than anything
#     def test_url_prefix_none(self):
#         kwargs = {
#             'url_prefix': None, 'use_ssl' : True, 'ssl_no_validate' : True
#         }
#         self.assertRaises(
#             elasticsearch.ElasticsearchException,
#             curator.get_client, **kwargs
#         )
#     def test_url_prefix_none_str(self):
#         kwargs = {
#             'url_prefix': 'None', 'use_ssl' : True, 'ssl_no_validate' : True
#         }
#         self.assertRaises(
#             elasticsearch.ElasticsearchException,
#             curator.get_client, **kwargs
#         )
#     def test_master_only_multiple_hosts(self):
#         kwargs = {
#             'url_prefix': '', 'master_only' : True,
#             'hosts' : ['127.0.0.1', '127.0.0.1']
#         }
#         self.assertRaises(
#             curator.ConfigurationError,
#             curator.get_client, **kwargs
#         )
#     def test_host_with_hosts(self):
#         kwargs = {
#             'url_prefix': '',
#             'host' : '127.0.0.1',
#             'hosts' : ['127.0.0.2'],
#         }
#         self.assertRaises(
#             curator.ConfigurationError,
#             curator.get_client, **kwargs
#         )
#     def test_certificate_logic(self):
#         kwargs = { 'use_ssl' : True, 'certificate' : 'mycert.pem' }
#         self.assertRaises(
#             elasticsearch.ElasticsearchException,
#             curator.get_client, **kwargs
#         )
#     def test_client_cert_logic(self):
#         kwargs = { 'use_ssl' : True, 'client_cert' : 'myclientcert.pem' }
#         self.assertRaises(
#             elasticsearch.ElasticsearchException,
#             curator.get_client, **kwargs
#         )
#     def test_client_key_logic(self):
#         kwargs = { 'use_ssl' : True, 'client_key' : 'myclientkey.pem' }
#         self.assertRaises(
#             elasticsearch.ElasticsearchException,
#             curator.get_client, **kwargs
#         )
#     def test_certificate_no_verify_logic(self):
#         kwargs = { 'use_ssl' : True, 'ssl_no_validate' : True }
#         self.assertRaises(
#             elasticsearch.ElasticsearchException,
#             curator.get_client, **kwargs
#         )

# class TestShowDryRun(TestCase):
#     # For now, since it's a pain to capture logging output, this is just a
#     # simple code coverage run
#     def test_index_list(self):
#         client = Mock()
#         client.info.return_value = {'version': {'number': '5.0.0'} }
#         client.indices.get_settings.return_value = testvars.settings_two
#         client.cluster.state.return_value = testvars.clu_state_two
#         client.indices.stats.return_value = testvars.stats_two
#         client.field_stats.return_value = testvars.fieldstats_two
#         il = curator.IndexList(client)
#         self.assertIsNone(curator.show_dry_run(il, 'test_action'))

# class TestGetRepository(TestCase):
#     def test_get_repository_missing_arg(self):
#         client = Mock()
#         client.snapshot.get_repository.return_value = {}
#         self.assertEqual({}, curator.get_repository(client))
#     def test_get_repository_positive(self):
#         client = Mock()
#         client.snapshot.get_repository.return_value = testvars.test_repo
#         self.assertEqual(testvars.test_repo,
#             curator.get_repository(client, repository=testvars.repo_name))
#     def test_get_repository_transporterror_negative(self):
#         client = Mock()
#         client.snapshot.get_repository.side_effect = elasticsearch.TransportError(503,'foo','bar')
#         self.assertRaises(
#             curator.CuratorException,
#             curator.get_repository, client, repository=testvars.repo_name
#         )
#     def test_get_repository_notfounderror_negative(self):
#         client = Mock()
#         client.snapshot.get_repository.side_effect = elasticsearch.NotFoundError(404,'foo','bar')
#         self.assertRaises(
#             curator.CuratorException,
#             curator.get_repository, client, repository=testvars.repo_name
#         )
#     def test_get_repository__all_positive(self):
#         client = Mock()
#         client.snapshot.get_repository.return_value = testvars.test_repos
#         self.assertEqual(testvars.test_repos, curator.get_repository(client))

# class TestGetSnapshot(TestCase):
#     def test_get_snapshot_missing_repository_arg(self):
#         client = Mock()
#         self.assertRaises(
#             curator.MissingArgument,
#             curator.get_snapshot, client, snapshot=testvars.snap_name
#         )
#     def test_get_snapshot_positive(self):
#         client = Mock()
#         client.snapshot.get.return_value = testvars.snapshot
#         self.assertEqual(
#             testvars.snapshot, curator.get_snapshot(
#                 client, repository=testvars.repo_name, snapshot=testvars.snap_name))
#     def test_get_snapshot_transporterror_negative(self):
#         client = Mock()
#         client.snapshot.get_repository.return_value = testvars.test_repo
#         client.snapshot.get.side_effect = testvars.four_oh_one
#         self.assertRaises(
#             curator.FailedExecution,
#             curator.get_snapshot, client,
#             repository=testvars.repo_name, snapshot=testvars.snap_name
#         )
#     def test_get_snapshot_notfounderror_negative(self):
#         client = Mock()
#         client.snapshot.get_repository.return_value = testvars.test_repo
#         client.snapshot.get.side_effect = elasticsearch.NotFoundError(404, 'Snapshot not found')
#         self.assertRaises(
#             curator.FailedExecution,
#             curator.get_snapshot, client,
#             repository=testvars.repo_name, snapshot=testvars.snap_name
#         )

# class TestGetSnapshotData(TestCase):
#     def test_missing_repo_arg(self):
#         client = Mock()
#         self.assertRaises(curator.MissingArgument, curator.get_snapshot_data, client)
#     def test_return_data(self):
#         client = Mock()
#         client.snapshot.get.return_value = testvars.snapshots
#         client.snapshot.get_repository.return_value = testvars.test_repo
#         self.assertEqual(
#             testvars.snapshots['snapshots'],
#             curator.get_snapshot_data(client, repository=testvars.repo_name)
#         )
#     def test_raises_exception_onfail(self):
#         client = Mock()
#         client.snapshot.get.return_value = testvars.snapshots
#         client.snapshot.get.side_effect = testvars.four_oh_one
#         client.snapshot.get_repository.return_value = testvars.test_repo
#         self.assertRaises(
#             curator.FailedExecution,
#             curator.get_snapshot_data, client, repository=testvars.repo_name
#         )

# class TestSnapshotInProgress(TestCase):
#     def test_all_snapshots_for_in_progress(self):
#         client = Mock()
#         client.snapshot.get.return_value = testvars.inprogress
#         client.snapshot.get_repository.return_value = testvars.test_repo
#         self.assertEqual(
#             'snapshot-2015.03.01',
#             curator.snapshot_in_progress(client, repository=testvars.repo_name)
#         )
#     def test_specified_snapshot_in_progress(self):
#         client = Mock()
#         client.snapshot.get.return_value = testvars.inprogress
#         client.snapshot.get_repository.return_value = testvars.test_repo
#         self.assertEqual(
#             'snapshot-2015.03.01',
#             curator.snapshot_in_progress(
#                 client, repository=testvars.repo_name,
#                 snapshot='snapshot-2015.03.01'
#             )
#         )
#     def test_specified_snapshot_in_progress_negative(self):
#         client = Mock()
#         client.snapshot.get.return_value = testvars.inprogress
#         client.snapshot.get_repository.return_value = testvars.test_repo
#         self.assertFalse(
#             curator.snapshot_in_progress(
#                 client, repository=testvars.repo_name,
#                 snapshot=testvars.snap_name
#             )
#         )
#     def test_all_snapshots_for_in_progress_negative(self):
#         client = Mock()
#         client.snapshot.get.return_value = testvars.snapshots
#         client.snapshot.get_repository.return_value = testvars.test_repo
#         self.assertFalse(
#             curator.snapshot_in_progress(client, repository=testvars.repo_name)
#         )
#     def test_for_multiple_in_progress(self):
#         client = Mock()
#         client.snapshot.get.return_value = testvars.highly_unlikely
#         client.snapshot.get_repository.return_value = testvars.test_repo
#         self.assertRaises(
#             curator.CuratorException,
#             curator.snapshot_in_progress, client, repository=testvars.repo_name
#         )

# class TestCreateSnapshotBody(TestCase):
#     def test_create_snapshot_body_empty_arg(self):
#         self.assertFalse(curator.create_snapshot_body([]))
#     def test_create_snapshot_body__all_positive(self):
#         self.assertEqual(testvars.snap_body_all, curator.create_snapshot_body('_all'))
#     def test_create_snapshot_body_positive(self):
#         self.assertEqual(testvars.snap_body, curator.create_snapshot_body(testvars.named_indices))

# class TestCreateRepoBody(TestCase):
#     def test_missing_repo_type(self):
#         self.assertRaises(curator.MissingArgument,
#             curator.create_repo_body
#         )

#     def test_s3(self):
#         body = curator.create_repo_body(repo_type='s3')
#         self.assertEqual(body['type'], 's3')

# class TestCreateRepository(TestCase):
#     def test_missing_arg(self):
#         client = Mock()
#         self.assertRaises(curator.MissingArgument,
#             curator.create_repository, client
#         )

#     def test_empty_result_call(self):
#         client = Mock()
#         client.snapshot.get_repository.return_value = None
#         self.assertTrue(curator.create_repository(client, repository="repo", repo_type="fs"))

#     def test_repo_not_in_results(self):
#         client = Mock()
#         client.snapshot.get_repository.return_value = {'not_your_repo':{'foo':'bar'}}
#         self.assertTrue(curator.create_repository(client, repository="repo", repo_type="fs"))

#     def test_repo_already_in_results(self):
#         client = Mock()
#         client.snapshot.get_repository.return_value = {'repo':{'foo':'bar'}}
#         self.assertRaises(curator.FailedExecution,
#             curator.create_repository, client, repository="repo", repo_type="fs"
#         )

#     def test_raises_exception(self):
#         client = Mock()
#         client.snapshot.get_repository.return_value = {'not_your_repo':{'foo':'bar'}}
#         client.snapshot.create_repository.side_effect = elasticsearch.TransportError(
#             500, "Error message", {"message":"Error"})
#         self.assertRaises(
#             curator.FailedExecution, curator.create_repository,
#             client, repository="repo", repo_type="fs"
#         )

# class TestRepositoryExists(TestCase):
#     def test_missing_arg(self):
#         client = Mock()
#         self.assertRaises(curator.MissingArgument,
#             curator.repository_exists, client
#         )

#     def test_repository_in_results(self):
#         client = Mock()
#         client.snapshot.get_repository.return_value = {'repo':{'foo':'bar'}}
#         self.assertTrue(curator.repository_exists(client, repository="repo"))

#     def test_repo_not_in_results(self):
#         client = Mock()
#         client.snapshot.get_repository.return_value = {'not_your_repo':{'foo':'bar'}}
#         self.assertFalse(curator.repository_exists(client, repository="repo"))

# class TestRepositoryFs(TestCase):
#     def test_passing(self):
#         client = Mock()
#         client.snapshot.verify_repository.return_value = testvars.verified_nodes
#         self.assertIsNone(
#             curator.test_repo_fs(client, repository=testvars.repo_name))
#     def test_raises_404(self):
#         client = Mock()
#         client.snapshot.verify_repository.return_value = testvars.verified_nodes
#         client.snapshot.verify_repository.side_effect = testvars.four_oh_four
#         self.assertRaises(curator.ActionError, curator.test_repo_fs, client,
#             repository=testvars.repo_name)
#     def test_raises_401(self):
#         client = Mock()
#         client.snapshot.verify_repository.return_value = testvars.verified_nodes
#         client.snapshot.verify_repository.side_effect = testvars.four_oh_one
#         self.assertRaises(curator.ActionError, curator.test_repo_fs, client,
#             repository=testvars.repo_name)
#     def test_raises_other(self):
#         client = Mock()
#         client.snapshot.verify_repository.return_value = testvars.verified_nodes
#         client.snapshot.verify_repository.side_effect = testvars.fake_fail
#         self.assertRaises(curator.ActionError, curator.test_repo_fs, client,
#             repository=testvars.repo_name)

# class TestSafeToSnap(TestCase):
#     def test_missing_arg(self):
#         client = Mock()
#         self.assertRaises(curator.MissingArgument,
#             curator.safe_to_snap, client
#         )
#     def test_in_progress_fail(self):
#         client = Mock()
#         client.snapshot.get.return_value = testvars.inprogress
#         client.snapshot.get_repository.return_value = testvars.test_repo
#         client.tasks.get.return_value = testvars.no_snap_tasks
#         self.assertFalse(
#             curator.safe_to_snap(
#                 client, repository=testvars.repo_name,
#                 retry_interval=0, retry_count=1
#             )
#         )
#     def test_ongoing_tasks_fail(self):
#         client = Mock()
#         client.snapshot.get.return_value = testvars.snapshots
#         client.snapshot.get_repository.return_value = testvars.test_repo
#         client.tasks.get.return_value = testvars.snap_task
#         self.assertFalse(
#             curator.safe_to_snap(
#                 client, repository=testvars.repo_name,
#                 retry_interval=0, retry_count=1
#             )
#         )
#     def test_in_progress_pass(self):
#         client = Mock()
#         client.snapshot.get.return_value = testvars.snapshots
#         client.snapshot.get_repository.return_value = testvars.test_repo
#         client.tasks.get.return_value = testvars.no_snap_tasks
#         self.assertTrue(
#             curator.safe_to_snap(
#                 client, repository=testvars.repo_name,
#                 retry_interval=0, retry_count=1
#             )
#         )

# class TestSnapshotRunning(TestCase):
#     def test_true(self):
#         client = Mock()
#         client.snapshot.status.return_value = testvars.snap_running
#         self.assertTrue(curator.snapshot_running(client))
#     def test_false(self):
#         client = Mock()
#         client.snapshot.status.return_value = testvars.nosnap_running
#         self.assertFalse(curator.snapshot_running(client))
#     def test_raises_exception(self):
#         client = Mock()
#         client.snapshot.status.return_value = testvars.nosnap_running
#         client.snapshot.status.side_effect = testvars.fake_fail
#         self.assertRaises(
#             curator.FailedExecution, curator.snapshot_running, client)



# class TestValidateFilters(TestCase):
#     def test_snapshot_with_index_filter(self):
#         self.assertRaises(
#             curator.ConfigurationError,
#             curator.validate_filters,
#             'delete_snapshots',
#             [{'filtertype': 'kibana'}]
#         )
#     def test_index_with_snapshot_filter(self):
#         self.assertRaises(
#             curator.ConfigurationError,
#             curator.validate_filters,
#             'delete_indices',
#             [{'filtertype': 'state', 'state': 'SUCCESS'}]
#         )


# class TestVerifyClientObject(TestCase):

#     def test_is_client_object(self):
#         test = elasticsearch.Elasticsearch()
#         self.assertIsNone(curator.verify_client_object(test))

#     def test_is_not_client_object(self):
#         test = 'not a client object'
#         self.assertRaises(TypeError, curator.verify_client_object, test)

#     def test_is_a_subclass_client_object(self):
#         class ElasticsearchSubClass(elasticsearch.Elasticsearch):
#             pass
#         test = ElasticsearchSubClass()
#         self.assertIsNone(curator.verify_client_object(test))

# class TestRollableAlias(TestCase):
#     def test_return_false_if_no_alias(self):
#         client = Mock()
#         client.indices.get_alias.return_value = {}
#         client.indices.get_alias.side_effect = elasticsearch.NotFoundError
#         self.assertFalse(curator.rollable_alias(client, 'foo'))
#     def test_return_false_too_many_indices(self):
#         client = Mock()
#         client.indices.get_alias.return_value = testvars.not_rollable_multiple
#         self.assertFalse(curator.rollable_alias(client, 'foo'))
#     def test_return_false_non_numeric(self):
#         client = Mock()
#         client.indices.get_alias.return_value = testvars.not_rollable_non_numeric
#         self.assertFalse(curator.rollable_alias(client, 'foo'))
#     def test_return_true_two_digits(self):
#         client = Mock()
#         client.indices.get_alias.return_value = testvars.is_rollable_2digits
#         self.assertTrue(curator.rollable_alias(client, 'foo'))
#     def test_return_true_hypenated(self):
#         client = Mock()
#         client.indices.get_alias.return_value = testvars.is_rollable_hypenated
#         self.assertTrue(curator.rollable_alias(client, 'foo'))

# class TestHealthCheck(TestCase):
#     def test_no_kwargs(self):
#         client = Mock()
#         self.assertRaises(
#             curator.MissingArgument, curator.health_check, client
#         )
#     def test_key_value_match(self):
#         client = Mock()
#         client.cluster.health.return_value = testvars.cluster_health
#         self.assertTrue(
#             curator.health_check(client, status='green')
#         )
#     def test_key_value_no_match(self):
#         client = Mock()
#         client.cluster.health.return_value = testvars.cluster_health
#         self.assertFalse(
#             curator.health_check(client, status='red')
#         )
#     def test_key_not_found(self):
#         client = Mock()
#         client.cluster.health.return_value = testvars.cluster_health
#         self.assertRaises(
#             curator.ConfigurationError,
#             curator.health_check, client, foo='bar'
#         )

# class TestSnapshotCheck(TestCase):
#     def test_fail_to_get_snapshot(self):
#         client = Mock()
#         client.snapshot.get.side_effect = testvars.fake_fail
#         self.assertRaises(
#             curator.CuratorException, curator.snapshot_check, client
#         )
#     def test_in_progress(self):
#         client = Mock()
#         client.snapshot.get.return_value = testvars.oneinprogress
#         self.assertFalse(
#             curator.snapshot_check(client,
#                 repository='foo', snapshot=testvars.snap_name)
#         )
#     def test_success(self):
#         client = Mock()
#         client.snapshot.get.return_value = testvars.snapshot
#         self.assertTrue(
#             curator.snapshot_check(client,
#                 repository='foo', snapshot=testvars.snap_name)
#         )
#     def test_partial(self):
#         client = Mock()
#         client.snapshot.get.return_value = testvars.partial
#         self.assertTrue(
#             curator.snapshot_check(client,
#                 repository='foo', snapshot=testvars.snap_name)
#         )
#     def test_failed(self):
#         client = Mock()
#         client.snapshot.get.return_value = testvars.failed
#         self.assertTrue(
#             curator.snapshot_check(client,
#                 repository='foo', snapshot=testvars.snap_name)
#         )
#     def test_other(self):
#         client = Mock()
#         client.snapshot.get.return_value = testvars.othersnap
#         self.assertTrue(
#             curator.snapshot_check(client,
#                 repository='foo', snapshot=testvars.snap_name)
#         )

# class TestRestoreCheck(TestCase):
#     def test_fail_to_get_recovery(self):
#         client = Mock()
#         client.indices.recovery.side_effect = testvars.fake_fail
#         self.assertRaises(
#             curator.CuratorException, curator.restore_check, client, []
#         )
#     def test_incomplete_recovery(self):
#         client = Mock()
#         client.indices.recovery.return_value = testvars.unrecovered_output
#         self.assertFalse(
#             curator.restore_check(client, testvars.named_indices)
#         )
#     def test_completed_recovery(self):
#         client = Mock()
#         client.indices.recovery.return_value = testvars.recovery_output
#         self.assertTrue(
#             curator.restore_check(client, testvars.named_indices)
#         )
#     def test_empty_recovery(self):
#         client = Mock()
#         client.indices.recovery.return_value = {}
#         self.assertFalse(
#             curator.restore_check(client, testvars.named_indices)
#         )
#     def test_fix_966(self):
#         client = Mock()
#         client.indices.recovery.return_value = testvars.recovery_966
#         self.assertTrue(
#             curator.restore_check(client, testvars.index_list_966)
#         )

# class TestTaskCheck(TestCase):
#     def test_bad_task_id(self):
#         client = Mock()
#         client.tasks.get.side_effect = testvars.fake_fail
#         self.assertRaises(
#             curator.CuratorException, curator.task_check, client, 'foo'
#         )
#     def test_incomplete_task(self):
#         client = Mock()
#         client.tasks.get.return_value = testvars.incomplete_task
#         self.assertFalse(
#             curator.task_check(client, task_id=testvars.generic_task['task'])
#         )
#     def test_complete_task(self):
#         client = Mock()
#         client.tasks.get.return_value = testvars.completed_task
#         self.assertTrue(
#             curator.task_check(client, task_id=testvars.generic_task['task'])
#         )

# class TestWaitForIt(TestCase):
#     def test_bad_action(self):
#         client = Mock()
#         self.assertRaises(
#             curator.ConfigurationError, curator.wait_for_it, client, 'foo')
#     def test_reindex_action_no_task_id(self):
#         client = Mock()
#         self.assertRaises(
#             curator.MissingArgument, curator.wait_for_it,
#             client, 'reindex')
#     def test_snapshot_action_no_snapshot(self):
#         client = Mock()
#         self.assertRaises(
#             curator.MissingArgument, curator.wait_for_it,
#             client, 'snapshot', repository='foo')
#     def test_snapshot_action_no_repository(self):
#         client = Mock()
#         self.assertRaises(
#             curator.MissingArgument, curator.wait_for_it,
#             client, 'snapshot', snapshot='foo')
#     def test_restore_action_no_indexlist(self):
#         client = Mock()
#         self.assertRaises(
#             curator.MissingArgument, curator.wait_for_it,
#             client, 'restore')
#     def test_reindex_action_bad_task_id(self):
#         client = Mock()
#         client.tasks.get.return_value = {'a':'b'}
#         client.tasks.get.side_effect = testvars.fake_fail
#         self.assertRaises(
#             curator.CuratorException, curator.wait_for_it,
#             client, 'reindex', task_id='foo')
#     def test_reached_max_wait(self):
#         client = Mock()
#         client.cluster.health.return_value = {'status':'red'}
#         self.assertRaises(curator.ActionTimeout,
#             curator.wait_for_it, client, 'replicas',
#                 wait_interval=1, max_wait=1
#         )

# class TestNodeRoles(TestCase):
#     def test_node_roles(self):
#         node_id = u'my_node'
#         expected = ['data']
#         client = Mock()
#         client.nodes.info.return_value = {
#             u'nodes':{node_id:{u'roles':testvars.data_only_node_role}}}
#         self.assertEqual(expected, curator.node_roles(client, node_id))

# class TestSingleDataPath(TestCase):
#     def test_single_data_path(self):
#         node_id = 'my_node'
#         client = Mock()
#         client.nodes.stats.return_value = {u'nodes':{node_id:{u'fs':{u'data':[u'one']}}}}
#         self.assertTrue(curator.single_data_path(client, node_id))
#     def test_two_data_paths(self):
#         node_id = 'my_node'
#         client = Mock()
#         client.nodes.stats.return_value = {u'nodes':{node_id:{u'fs':{u'data':[u'one',u'two']}}}}
#         self.assertFalse(curator.single_data_path(client, node_id))

# class TestNameToNodeId(TestCase):
#     def test_positive(self):
#         node_id = 'node_id'
#         node_name = 'node_name'
#         client = Mock()
#         client.nodes.stats.return_value = {u'nodes':{node_id:{u'name':node_name}}}
#         self.assertEqual(node_id, curator.name_to_node_id(client, node_name))
#     def test_negative(self):
#         node_id = 'node_id'
#         node_name = 'node_name'
#         client = Mock()
#         client.nodes.stats.return_value = {u'nodes':{node_id:{u'name':node_name}}}
#         self.assertIsNone(curator.name_to_node_id(client, 'wrong_name'))

# class TestNodeIdToName(TestCase):
#     def test_negative(self):
#         client = Mock()
#         client.nodes.stats.return_value = {u'nodes':{'my_node_id':{u'name':'my_node_name'}}}
#         self.assertIsNone(curator.node_id_to_name(client, 'not_my_node_id'))
