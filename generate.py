from rich.console import Console
console = Console()

print("Welcome To The Country Adding Script: ")

name = input("enter the name of the country: ")
capital = input('enter the capital of the country: ')
population = input('enter the population of the country: ')
language = input('enter the current official languages of this country: ')
currency = input('enter the current currency of your country: ')
index = input('enter the index of your country: ')
format = {
            "country": name,
            "capital": capital,
            "population": population,
            "language": language,
            "currency": currency,
            "index": index,
}
import json
console.print(format)
f  = open("./dataset/" + name + '.json', 'a')
f.write(json.dumps(format))