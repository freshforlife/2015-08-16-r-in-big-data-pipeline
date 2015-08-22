import luigi
from luigi.file import LocalTarget
from luigi.hive import HiveTableTarget
from luigi.contrib.hdfs import HdfsTarget
import subprocess
import sys

class HiveTask1(luigi.ExternalTask):
    timestamp = luigi.DateParameter(is_global=True)
    def output(self):
        return HdfsTarget('/user/storage/externaljob/timestamp=%s' % self.timestamp.strftime('%Y%m%d'))

class RTask(luigi.Task):
    timestamp = HiveTask1.timestamp
    def requires(self):
        return HiveTask1()
    def run(self):
        subprocess.call('Rscript awesome.R %s' % self.timestamp.strftime('%Y%m%d'),shell=True)
    def output(self):
        return LocalTarget('awesome_is_here_%s.txt' % self.timestamp.strftime('%Y%m%d'))

class HiveTask2(luigi.Task):
    timestamp=HiveTask1.timestamp
    def requires(self):
        return RTask()
    def run(self):
        subprocess.call('Rscript update2hive.R %s' % self.timestamp.strftime('%Y%m%d'),shell=True)
    def output(self):
        return HdfsTarget('/user/hive/warehouse/awesome/timestamp=%s' % self.timestamp.strftime('%Y%m%d'))


if __name__ == '__main__':
    luigi.run()1