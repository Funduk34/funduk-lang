import sys
import re

def validate_worship(lines):
    if not lines:
        raise SyntaxError("UnpoliteNutError: Файл пуст! Фундук оскорблен.")
    first_line = lines[0].strip().lower()
    last_line = lines[-1].strip().lower()
    if first_line != "здравствуйте глубокоуважаемый фундук":
        raise SyntaxError("UnpoliteNutError: Вы не поздоровались с Фундуком! Первая строка должна быть: 'Здравствуйте глубокоуважаемый Фундук'")
    if last_line != "спасибо за орехи до свидания":
        raise SyntaxError("UnpoliteNutError: Вы не попрощались с Фундуком! Последняя строка должна быть: 'Спасибо за орехи до свидания'")

def validate_case_alternation(text):
    words = re.findall(r'[a-zA-Zа-яА-ЯёЁ0-9_]+', text)
    for index, word in enumerate(words):
        should_be_upper = (index % 2 == 0)
        is_upper = word[0].isupper()
        if should_be_upper and not is_upper:
            raise SyntaxError(f"CaseAnarchyError: Слово '{word}' (позиция {index+1}) должно начинаться с ЗАГЛАВНОЙ буквы!")
        if not should_be_upper and is_upper:
            raise SyntaxError(f"CaseAnarchyError: Слово '{word}' (позиция {index+1}) должно начинаться с МАЛЕНЬКОЙ буквы!")

def compile_funduk(source):
    lines = [l for l in source.splitlines() if l.strip()]
    validate_worship(lines)
    validate_case_alternation(source)
    
    body_lines = lines[1:-1]
    result = []
    
    for line in body_lines:
        lower_line = line.lower()
        if "выплюнуть фундук" in lower_line:
            tens = lower_line.count("фундучище") * 10
            ones = lower_line.count("фундучек")
            sub = lower_line.count("гнилушка")
            char_code = tens + ones - sub
            indent = len(line) - len(line.lstrip())
            result.append(" " * indent + f"print(chr({char_code}), end='')")
        else:
            code_line = lower_line
            code_line = re.sub(r'\bфундук чини\b', 'def', code_line)
            code_line = re.sub(r'\bфундук хавен\b', 'while', code_line)
            code_line = re.sub(r'\bфундук орех\b', 'if', code_line)
            code_line = re.sub(r'\bиначе орех\b', 'elif', code_line)
            code_line = re.sub(r'\bсовсем гнилой\b', 'else', code_line)
            code_line = re.sub(r'\bфундучище\b', '=', code_line)
            code_line = re.sub(r'\bжареный фундук\b', 'print', code_line)
            code_line = re.sub(r'\bвскопать\b', 'input', code_line)
            code_line = re.sub(r'\bскорлупа\b', 'pass', code_line)
            code_line = re.sub(r'\bрасколоть\b', 'break', code_line)
            code_line = re.sub(r'\bорешек\b', ':', code_line)
            code_line = re.sub(r'\bфундуковать\b', 'import', code_line)
            result.append(code_line)
            
    return "\n".join(result)

def main():
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
    else:
        target_file = "script.fnd"
    
    try:
        with open(target_file, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Файл {target_file} не найден!")
        return

    try:
        python_code = compile_funduk(content)
        exec(python_code)
    except Exception as e:
        print(f"ОШИБКА ФУНДУКА: {e}")

if __name__ == "__main__":
    main()