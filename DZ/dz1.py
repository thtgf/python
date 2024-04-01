text = ("Ежевику для ежат Принесли два ежат. Принесли два ежа. Еживику еле-еле Ежата возле ели съели.")
text = text.split(" ")
i = 0
for word in text:

    if word[0].lower() == "е":

        i = i+1;

print (i)