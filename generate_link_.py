from flask import Flask, request, jsonify, render_template


def create_whatsapp_link(phone_number):
   # Substitua 'SeuNúmero' pelo número do telefone fornecido
   whatsapp_link = f"https://api.whatsapp.com/send?phone={phone_number}"
   return whatsapp_link




app = Flask(__name__)

@app.route('/whatsapp', methods=['GET'])
def get_whatsapp_link():
  #  data = request.get_json()
   phone_number = '55034991304873'
   if phone_number:
       whatsapp_link = create_whatsapp_link(phone_number)
       #  jsonify({'whatsapp_link': whatsapp_link})
       return render_template(f'''

       <!DOCTYPE html>
       <html>
       <div>
        <p>Clique: </p><a>{whatsapp_link}</a>
       </div>

       </html>
       
       
       ''')

  
if __name__ == "__main__":
   app.run(debug=True)
