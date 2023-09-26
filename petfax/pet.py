from flask import ( Blueprint, render_template ) 
import json 

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")


@bp.route('/<id>')

def index(id): 
    if id:
        print(id)
        newpet={}
        for pet in pets: 
            if pet['pet_id'] == int(id):
                newpet = pet
            print(newpet)
                
        return render_template('pets/showpet.html', pet=newpet)
    else:

         return render_template('pets/index.html', pets=pets)





