# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'LegMinutesMetaData'
        db.create_table('phillyleg_legminutesmetadata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('legminutes', self.gf('django.db.models.fields.related.OneToOneField')(related_name='metadata', unique=True, to=orm['phillyleg.LegMinutes'])),
        ))
        db.send_create_signal('phillyleg', ['LegMinutesMetaData'])

        # Adding M2M table for field words on 'LegMinutesMetaData'
        db.create_table('phillyleg_legminutesmetadata_words', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('legminutesmetadata', models.ForeignKey(orm['phillyleg.legminutesmetadata'], null=False)),
            ('metadata_word', models.ForeignKey(orm['phillyleg.metadata_word'], null=False))
        ))
        db.create_unique('phillyleg_legminutesmetadata_words', ['legminutesmetadata_id', 'metadata_word_id'])


    def backwards(self, orm):
        
        # Deleting model 'LegMinutesMetaData'
        db.delete_table('phillyleg_legminutesmetadata')

        # Removing M2M table for field words on 'LegMinutesMetaData'
        db.delete_table('phillyleg_legminutesmetadata_words')


    models = {
        'phillyleg.councilmember': {
            'Meta': {'object_name': 'CouncilMember'},
            'headshot': ('django.db.models.fields.CharField', [], {'default': "'phillyleg/noun_project_416.png'", 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'phillyleg.councilmembersubscription': {
            'Meta': {'object_name': 'CouncilMemberSubscription'},
            'councilmember': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['phillyleg.CouncilMember']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subscription': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'councilmembers'", 'to': "orm['phillyleg.Subscription']"})
        },
        'phillyleg.keywordsubscription': {
            'Meta': {'object_name': 'KeywordSubscription'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'subscription': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'keywords'", 'to': "orm['phillyleg.Subscription']"})
        },
        'phillyleg.legaction': {
            'Meta': {'unique_together': "(('file', 'date_taken', 'description', 'notes'),)", 'object_name': 'LegAction'},
            'acting_body': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'date_taken': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'file': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'actions'", 'to': "orm['phillyleg.LegFile']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minutes': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'actions'", 'null': 'True', 'to': "orm['phillyleg.LegMinutes']"}),
            'motion': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'notes': ('django.db.models.fields.TextField', [], {})
        },
        'phillyleg.legfile': {
            'Meta': {'ordering': "['-key']", 'object_name': 'LegFile'},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'controlling_body': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'date_scraped': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'final_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'intro_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'key': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'last_scraped': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sponsors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'legislation'", 'symmetrical': 'False', 'to': "orm['phillyleg.CouncilMember']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'phillyleg.legfileattachment': {
            'Meta': {'unique_together': "(('file', 'url'),)", 'object_name': 'LegFileAttachment'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'file': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'attachments'", 'to': "orm['phillyleg.LegFile']"}),
            'fulltext': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'phillyleg.legfilemetadata': {
            'Meta': {'object_name': 'LegFileMetaData'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legfile': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'metadata'", 'unique': 'True', 'to': "orm['phillyleg.LegFile']"}),
            'mentioned_legfiles': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'references'", 'symmetrical': 'False', 'to': "orm['phillyleg.LegFile']"}),
            'words': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'references'", 'symmetrical': 'False', 'to': "orm['phillyleg.MetaData_Word']"})
        },
        'phillyleg.legkeys': {
            'Meta': {'object_name': 'LegKeys'},
            'continuation_key': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'phillyleg.legminutes': {
            'Meta': {'object_name': 'LegMinutes'},
            'date_taken': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'fulltext': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'})
        },
        'phillyleg.legminutesmetadata': {
            'Meta': {'object_name': 'LegMinutesMetaData'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legminutes': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'metadata'", 'unique': 'True', 'to': "orm['phillyleg.LegMinutes']"}),
            'words': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'references_in_minutes'", 'symmetrical': 'False', 'to': "orm['phillyleg.MetaData_Word']"})
        },
        'phillyleg.metadata_word': {
            'Meta': {'object_name': 'MetaData_Word'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'phillyleg.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_sent': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['phillyleg']
