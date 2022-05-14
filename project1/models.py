from pyexpat import model
from statistics import mode
from django.db import models


class member(models.Model):
    given_name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date_of_birth = models.DateField()

    class Meta:
        """
            The tip below of the schema].[model came from here:
            http://nightlyclosures.com/2018/01/08/working-with-mssql-in-django/
        """
        
        db_table = 'project1].[member'


class PurchaseOrderDetail(models.Model):
    purchaseorderid = models.IntegerField(db_column='PurchaseOrderID', primary_key=True)  # Field name made lowercase.
    linenumber = models.SmallIntegerField(db_column='LineNumber')  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    orderqty = models.SmallIntegerField(db_column='OrderQty', blank=True, null=True)  # Field name made lowercase.
    receivedqty = models.FloatField(db_column='ReceivedQty', blank=True, null=True)  # Field name made lowercase.
    rejectedqty = models.FloatField(db_column='RejectedQty', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.
    rowguid = models.CharField(max_length=36)
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    linetotal = models.DecimalField(db_column='LineTotal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stockedqty = models.FloatField(db_column='StockedQty', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project1].[PurchaseOrderDetail'
        unique_together = (('purchaseorderid', 'linenumber'),)