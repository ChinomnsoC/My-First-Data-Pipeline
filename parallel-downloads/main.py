import luigi
from luigi import Task, LocalTarget
from luigi.contrib.s3 import S3Target


class DownloadOrders(Task):
    def output(self):
        return LocalTarget('orders.csv')

    def run(self):
        with self.output().open('w') as f:
            f.write('to do...')


class DownloadSales(Task):
    def output(self): 
        return LocalTarget('sales.csv')

    def run(self):
        with self.output().open('w') as f:
            f.write('to do...')


class DownloadInventory(Task):
    def output(self):
        return LocalTarget('inventory.csv')

    def run(self):
        with self.output().open('w') as f:
            f.write('to do...')


class UploadS3(Task):
    def requires(self):
        return [DownloadOrders(),
                DownloadSales(),
                DownloadInventory()]

    def output(self):
        return S3Target('s3://playground.learning/luigi-demo/parallel-tasks/chinomnsos-s3output.txt')

    def run(self):
        with self.output().open('w') as f:
            f.write('to do...')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    luigi.run(['UploadS3', '--local-scheduler'])

