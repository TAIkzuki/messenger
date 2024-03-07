from flask import Flask, request, jsonify
from mongoengine import connect
from models import Dialog

app = Flask(__name__)
connect('dialog_app')

class DialogController:
    def index(self, user_id):
        dialogs = Dialog.objects(dialogParticipants__user=user_id).\
                  exclude('messages').\
                  only('dialogParticipants', 'lastMessage')
        return jsonify(dialogs), 200

    def delete(self, dialog_id):
        dialog = Dialog.objects.get_or_404(id=dialog_id)
        dialog.delete()
        return jsonify(message='Dialog has been deleted'), 200

    def create(self):
        data = request.json
        dialog = Dialog(**data)
        dialog.save()
        return jsonify(dialog), 201

    def get(self, dialog_id):
        dialog = Dialog.objects.get_or_404(id=dialog_id)
        return jsonify(dialog), 200

dialog_controller = DialogController()

@app.route('/dialogs/<string:user_id>', methods=['GET'])
def index(user_id):
    return dialog_controller.index(user_id)

@app.route('/dialogs/<string:dialog_id>', methods=['DELETE'])
def delete(dialog_id):
    return dialog_controller.delete(dialog_id)

@app.route('/dialogs', methods=['POST'])
def create():
    return dialog_controller.create()

@app.route('/dialogs/<string:dialog_id>', methods=['GET'])
def get(dialog_id):
    return dialog_controller.get(dialog_id)

if __name__ == '__main__':
    app.run(debug=True)
