from django.contrib import admin
from pgmanager.models import EC2Instance, BestScore

class EC2InstanceAdmin(admin.ModelAdmin):
	pass

class BestScoreAdmin(admin.ModelAdmin):
	pass

admin.site.register(EC2Instance, EC2InstanceAdmin)
admin.site.register(BestScore, BestScoreAdmin)
