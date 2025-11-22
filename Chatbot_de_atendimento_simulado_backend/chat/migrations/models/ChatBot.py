from django.db import models 

class Message(models.Model):
    
    user_profile = models.CharField(max_length=1, choices=[('A', 'Usuário A'), ('B', 'Usuário B')])

    sender = models.CharField(max_length=10, choices=[
        ('A', 'Usuário A'), 
        ('B', 'Usuário B'),
        ('Backend', 'Sistema Backend')
        ])
