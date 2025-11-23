from django.db import models

class Message(models.Model):
   
    users_pro = models.CharField(max_length=1, choices=[('A', 'Usuário A'), ('B', 'Usuário B')])
    
    
    sender = models.CharField(max_length=10, choices=[
        ('A', 'Usuário A'),
        ('B', 'Usuário B'),
        ('Backend', 'Sistema Backend')
    ])
    
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
        verbose_name = 'Mensagem de Chat'
        verbose_name_plural = 'Mensagens de Chat'

    def __str__(self):
        return f'[{self.timestamp.strftime("%Y-%m-%d %H:%M")}] {self.sender} ({self.user_profile}): {self.text[:30]}...'


MOCK_RESPONSES = {
    'A': 'Obrigado por seu contato. Em breve responderemos.',
    'B': 'Agradecemos a sua preferência. Retornaremos em breve.',
}