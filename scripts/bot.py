from discord_webhook import DiscordWebhook, DiscordEmbed

questionnaire_webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1149771983844810882/JYotV_QBjYAdNDzaIFdIOqZAFHTPl4XtylC6anUpb9OI7aFxkk9K8Z9LJBUItkIzNYNM")
order_webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1149810908340699176/ahQPkxkCMxP9SgKIPGyYaGX_fdwe9D2O_9xSi3z6GJyccUBBVSrvG1dYkhqmF-xv-7yx")
new_account_webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1149812465304076348/lk84ZYAqtEBYdOoFgcTtDWpDBtNU7hkHzJoHE738ob4309P417O_e_gJtD1a5tZweyvX")
host_webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1152704140737257554/Ik3JASjlnZ2xjifvG4NhcnkncmWLn585GNCAW5Xxia1J2t_kai8WGVGP1-cd4XeRLWkS")


def QuestionnaireBot(questionnaire_id, user_email):
    url = str("http://127.0.0.1:8000/admin/core/questionnaire/"+ str(questionnaire_id))
    embed = DiscordEmbed(title="New Questionnaire!!", description="", url= url)
    embed.add_embed_field(name="questionnaire ID", value=questionnaire_id, inline=False)
    embed.add_embed_field(name="email", value=user_email, inline=False)
    questionnaire_webhook.add_embed(embed)
    questionnaire_webhook.execute()

def OrderBot(order_id, user_email, pay_price):
    url = str("http://127.0.0.1:8000/admin/orders/order/"+ str(order_id))
    embed = DiscordEmbed(title="New Order!!", description="", url= url)
    embed.add_embed_field(name="order ID", value=order_id, inline=False)
    embed.add_embed_field(name="email", value=user_email, inline=False)
    embed.add_embed_field(name="pay", value=str(pay_price), inline=False)
    order_webhook.add_embed(embed)
    order_webhook.execute()

def NewUserBot(user_id, user_email, user_name):
    url = str("http://127.0.0.1:8000/admin/accounts/userproxy/"+ str(user_id))
    embed = DiscordEmbed(title="New User!!", description="", url= url)
    embed.add_embed_field(name="user ID", value=user_id, inline=False)
    embed.add_embed_field(name="user email", value=user_email, inline=False)
    embed.add_embed_field(name="welcome", value=user_name, inline=False)
    new_account_webhook.add_embed(embed)
    new_account_webhook.execute()

def HostBot():
    host_start_stop = False
    if host_start_stop:
        embed = DiscordEmbed(title="Server Up!!", description="", color="00FF00")
        embed.set_timestamp()
        host_webhook.add_embed(embed)
        host_webhook.execute()
    else:
        pass