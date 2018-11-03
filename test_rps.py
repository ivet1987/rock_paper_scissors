import rps
import pytest
import subprocess
import sys

def test_rock_is_valid_play():
    assert rps.is_valid_play("rock") is True

def test_paper_is_valid_play():
    assert rps.is_valid_play('paper') is True

def test_scissors_is_valid_play():
    assert rps.is_valid_play('scissors') is True

def test_lizard_is_invalid_play():
    assert rps.is_valid_play('lizard') is False

def test_computer_play_is_valid():
    for _ in range(2000):
        play = rps.generate_computer_play()
        assert rps.is_valid_play(play)

def test_computer_plays_randomly():
    plays = [rps.generate_computer_play() for _ in range(5000)]
    rocks = plays.count("rock")
    paper = plays.count("paper")
    scissors = plays.count("scissors")
    print(rocks, paper, scissors)  #pokud test selže, vypíše se mi kolik čeho (když dám rock > 3000)
    assert plays.count("rock") > 200
    assert plays.count("paper") > 200
    assert plays.count("scissors") > 200

def test_paper_beats_rock():
    result = rps.evaluate_game("paper", "rock")
    assert result == "human"

def test_rock_beats_scissors():
    result = rps.evaluate_game("rock", "scissors")
    assert result == "human"

def test_scissors_beats_paper():
    result = rps.evaluate_game("scissors", "paper")
    assert result == "human"

def test_paper_lose_scissor():
    result = rps.evaluate_game("paper", "scissors")
    assert result == "computer"

def test_scissors_lose_rock():
    result = rps.evaluate_game("scissors", "rock")
    assert result == "computer"

def test_rock_lose_paper():
    result = rps.evaluate_game("rock", "paper")
    assert result == "computer"

#řeknu aby pro test input dělal něco jiného než v kodu, udělám falešnou funkci input

def input_faked_rock(prompt): #prompt = otázka
    print(prompt)
    return "rock"

def input_faked_paper(prompt):
    print(prompt)
    return "paper"

def input_faked_scissors(prompt):
    print(prompt)
    return "scissors"



def test_full_game(capsys):     #fixtures, vždy když v rps.py je input, zavolá se input_faked_rock
    #monkeypatch.setattr("builtins.input", input_faked_rock)  #jakou část pythonu chceme podvrhnout a čím
    rps.main(input = input_faked_rock)
    captured = capsys.readouterr()
    assert "rock, paper, or scissors?" in captured.out

def test_full_game2(capsys):     #fixtures, vždy když v rps.py je input, zavolá se input_faked_rock
    #monkeypatch.setattr("builtins.input", input_faked_rock)  #jakou část pythonu chceme podvrhnout a čím
    rps.main(input = input_faked_paper)
    captured = capsys.readouterr()
    assert "rock, paper, or scissors?" in captured.out

def test_full_game3(capsys):     #fixtures, vždy když v rps.py je input, zavolá se input_faked_rock
    #monkeypatch.setattr("builtins.input", input_faked_rock)  #jakou část pythonu chceme podvrhnout a čím
    rps.main(input = input_faked_scissors)
    captured = capsys.readouterr()
    assert "rock, paper, or scissors?" in captured.out

"""
vlastní fixture:
@pytest.fixture
def fake_input_rock(monkeypatch):
    monkeypatch.setattr("builtins.input", input_faked_rock)

def test_full_game(capsys, fake_input_rock):
    rps.main()
    captured = capsys.readouterr()
    assert "rock, paper, or scissors?" in captured.out

def test_wrong_play_result_in_repeated_question(): #cp ... completed process
    #cp = subprocess.run(["python", "rps.py"], encoding = "cp1250", stdout = subprocess.PIPE) #cp1250 = utf-8
    cp = subprocess.run([sys.executable, "rps.py"],
                        encoding = "cp1250",
                        stdout = subprocess.PIPE,
                        input ="dragon\nrock\n",
                        check=True) #cp1250 = utf-8
    assert cp.stdout.count("rock, paper, or scissors?") == 2"""
