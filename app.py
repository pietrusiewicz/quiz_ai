from flask import Flask, render_template, request, jsonify
import csv
import ollama

app = Flask(__name__)

questions,llms = [], []

def load_questions():
    questions = []
    with open('questions.csv', mode='r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == '': continue
            try:
                questions.append({
                    "id": int(row["id"]),
                    "question": row["q"],
                    "options": [row["A"], row["B"], row["C"], row["D"]],
                    "answer": row["answer"]
                })
            except KeyError as e:
                print(f"Missing key in CSV: {e}")
                continue
    return questions

@app.route('/')
def index():
    return render_template('index.html', questions=questions, llms=llms)

@app.route('/reload-data')
def reload_data():
    global questions
    questions = load_questions()
    return jsonify({"status": "Data reloaded"})

@app.route('/submit', methods=['POST'])
def submit():
    answers = request.json['answers']
    correct_count = sum(1 for q in questions if answers[f'q{q["id"]}'] == q["answer"])
    return jsonify({"correct_count": correct_count, "total": len(questions)})

@app.route('/update_question/<int:qid>', methods=['POST'])
def update_question(qid):
    data = request.get_json()
    # Update the CSV file or perform other actions with the new data
    print("Updating question ID:", qid, "with data:", data)
    return jsonify({"status": "success", "message": "Question updated successfully"})

@app.route('/update_questions', methods=['POST'])
def update_questions():
    data = request.get_json()
    # Update the CSV file or perform other actions with the new data
    print("Updating questions with data:", data)
    with open('questions.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'question', 'option1','option2','option3','option4', 'answer'])
        writer.writeheader()
        for item in data:
            row = {}
            row['id'] = item['id']
            row['q'] = item['question']
            row['A'] = item['options'][0]
            row['B'] = item['options'][1]
            row['C'] = item['options'][2]
            row['D'] = item['options'][3]
            row['answer'] = item['answer']
            writer.writerow(row)
        # Perform update operation here
    
    print(data)
   #with open('questions.csv', mode='w', newline='', encoding='utf-8') as file:
    #    writer = csv.DictWriter(file, fieldnames=['id', 'question', 'option1','option2','option3','option4', 'answer'])

        # Zapisz nagłówek
    #    writer.writeheader()

        # Zapisz każdy element w liście
     #   for item in data:
      #      writer.writerow(item)

    print("Dane zostały zapisane do pliku questions.csv")
    return jsonify({"status": "success", "message": "Questions updated successfully"})

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    print(user_input)
    # Tutaj integracja z Ollamą - przykład (może wymagać dostosowania)
    model_llm = request.json.get('llm')
    response = ollama.generate(
        model=model_llm,  # np. 'llama2', 'mistral' itp.
        prompt=user_input
    )
    
    #print(response.__dir__())
    print(response.response)
    return jsonify({'response': response.response})

if __name__ == '__main__':
    questions = load_questions()  # Load questions when the app starts
    llms = list(map(lambda x:x.model, list(ollama.list())[0][1]))
    app.run(debug=True)