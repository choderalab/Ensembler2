__author__ = 'Patrick B. Grinaway'
import os
import MSMSeeder.distributed as msmseeder
import pyspark


class SparkDriver(object):
    """
    Driver class for the Spark version of MSMSeeder. Provides a higher-
    level interface for interacting with MSMSeeder.
    """
    _starting_templates = None
    _rdd_starting_templates = None
    _modeled_seeds = None
    _filtered_models = None
    _failed_seeds = None
    _implicit_refined_seeds = None

    def __init__(self, target_squence, spark_master, constrained_memory=True, executor_memory='5g', auto_initialize=True):
        self._target_sequence = target_squence
        spark_conf = pyspark.SparkConf()
        spark_conf.setMaster(spark_master)
        spark_conf.set("spark.executor.memory", executor_memory)
        self._spark_context = pyspark.SparkContext(conf=spark_conf)
        self._model_rdds = dict()
        if auto_initialize:
            self.initialize_with_blast()







    def initialize_with_blast(self, local=True, max_hits=1000):
        """
        Initializes the SparkDriver class with results from a BLAST query, up to max_hits
        using local blast if specified.
        """
        if local:
            self._starting_templates = msmseeder.blast_pdb_local(self._target_sequence, num_hits=max_hits)
        else:
            self._starting_templates = msmseeder.blast_pdb(self._target_sequence, num_hits=max_hits)
        self._rdd_starting_templates = self._spark_context.parallelize(self._starting_templates)


    def make_models(self):
        """
        Make the initial homology models using MODELLER. Use filtered templates, or, if none,
        starting templates
        """

        self._modeled_seeds = self._rdd_starting_templates.map(msmseeder.align_template_target).map(msmseeder.make_model)
        self._failed_seeds = self.

    def refine_implicit(self):








