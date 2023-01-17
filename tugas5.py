from flask import Flask, render_template
app = Flask(__name__)
@app.route('/hobiku/<string:nama>')
def getnama(nama):
 nama = "Nama Saya {}" .format(nama)
 hobi = ['futsal','main game','renang']
 return render_template('hobiku.html', hobi = hobi, nama = nama)
if __name__ == '__main__':
 app.run(debug=True)