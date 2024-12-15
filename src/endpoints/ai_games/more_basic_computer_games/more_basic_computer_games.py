## \file hypotez/src/endpoints/ai_games/101_basic_games/101_basic_games.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.endpoints.ai_games.101_basic_games 
	:platform: Windows, Unix
	:synopsis:

"""
import asyncio
import time
from pathlib import Path
import header
from src import gs

from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai import OpenAIModel

from src.utils.jjson import j_loads, j_loads_ns
from src.utils.file import get_filenames
from src.utils.printer import pprint



class MoreBasicGames():
	"""	"""
	lang:str
	bob:GoogleGenerativeAI
	alice:GoogleGenerativeAI
	base_path:Path = gs.path.endpoints / 'ai_games' / 'more_basic_computer_games'
	command_instruction:str 
	games_list:list = []

	def __init__(self, lanf:str = 'en'):
		""""""
		config  = j_loads_ns(self.base_path / 'more_basic_computer_games.json')
		self.lang = lang
		system_instruction = Path(self.base_path / 'assets' / 'instructions' / 'raw.txt').read_text(encoding='UTF-8')
		self.command_instruction = Path(self.base_path / 'assets' / 'instructions' / f'write_code.{self.lang}.md').read_text(encoding='UTF-8')
		self.bob = GoogleGenerativeAI(
                model_name=config.model_name,
                api_key=gs.credentials.gemini.onela,
                system_instruction = system_instruction,
            )
		self.load_games_list()

	def load_games_list(self):
		"""
		Генерация списка имен игр из файлов в каталоге 'rules'.
		Извлекает имя игры из каждого файла, приводя его к верхнему регистру и заменяя подчеркивания на пробелы.
		"""
		rules_files = get_filenames(self.base_path / self.lang / 'rules')
		for file_name in rules_files:
			game_name = file_name.split('_', 1)[1].split('.')[0]  # Разделяем по подчеркиванию и точке
			self.games_list.append(game_name.upper().replace('_', ' '))  # Преобразуем в верхний регистр и заменяем подчеркивания на пробелы
	
	async def generate_python_code(self):
		""""""
		for game in self.games_list:
			q = self.command_instruction.replace('<GAME>',f'<{game}>')
			print(game)
			response = await self.bob.ask(q)
			if response.startswith(('```', '```python')) and response.endswith(('```', '```\n')):
				# Удаление начальных ```
				response = response.lstrip('`')
				# Удаление начальных 'python' после кавычек
				if response.startswith('python'):
					response = response[len('python'):].lstrip()
				# Удаление закрывающих ```
				response = response.rstrip('`').rstrip()
			self.save_code(game , response)
			time.sleep(20)

	def save_code(self, game:str, code:str):
		""""""
		...
		output_file:Path = self.base_path / self.lang / 'py' / f'{game.lower().replace(' ','_')}.py'
		output_file.parent.mkdir(parents=True, exist_ok=True)
		output_file.write_text(code,encoding='UTF-8')
		print(f'saved {game}')

	def create_rules_files(self):
		""""""
		rules_files = [
		"1_artillery_3.ru.md",
		"2_baccarat.ru.md",
		"3_bible_quiz.ru.md",
		"4_big_6.ru.md",
		"5_binary.ru.md",
		"6_blackbox.ru.md",
		"7_bobstones.ru.txt",
		"8_bocce.ru.md",
		"9_boga_ii.ru.md",
		"10_bombrun.ru.md",
		"11_bridge_it.ru.md",
		"12_camel.ru.md",
		"13_chase.ru.md",
		"14_chuck_a_luck.ru.md",
		"15_close_encounters.ru.md",
		"16_column.ru.md",
		"17_concentration.ru.md",
		"18_condot.ru.md",
		"19_convoy.ru.md",
		"20_corral.ru.md",
		"21_countdown.ru.md",
		"22_cup.ru.md",
		"23_dealerx_5.ru.md",
		"24_deepspace.ru.md",
		"25_defuse.ru.md",
		"26_dodgem.ru.md",
		"27_doors.ru.md",
		"28_drag.ru.md",
		"29_eliza.ru.md",
		"30_father.ru.md",
		"31_flip.ru.md",
		"32_four_in_a_row.ru.md",
		"33_geowar.ru.md",
		"34_grand_prix.ru.md",
		"35_guess_it.ru.md",
		"36_icbm.ru.md",
		"37_inkblot.ru.md",
		"38_joust.ru.md",
		"39_jumping_balls.ru.md",
		"40_keno.ru.md",
		"41_lgame.ru.md",
		"42_life_expectancy.ru.md",
		"43_lissajous.ru.md",
		"44_magic_square.ru.md",
		"45_man_eating_rabbit.ru.md",
		"46_maneuvers.ru.md",
		"47_mastermind.ru.md",
		"48_masterbagels.ru.md",
		"49_matpuzzle.ru.md",
		"50_maze.ru.md",
		"51_minotaur.ru.md",
		"52_motorcycle_jump.ru.md",
		"53_nomad.ru.md",
		"54_not_one.ru.md",
		"55_obstacle.ru.md",
		"56_octrlx.ru.md",
		"57_pasart.ru.md",
		"58_pasart2.ru.md",
		"59_pinball.ru.md",
		"60_rabbit_chase.ru.md",
		"61_roadrace.ru.md",
		"62_rotate.ru.md",
		"63_safe.ru.md",
		"64_scales.ru.md",
		"65_schmoo.ru.md",
		"66_seabattle.ru.md",
		"67_seawar.ru.md",
		"68_shoot.ru.md",
		"69_smash.ru.md",
		"70_strike_9.ru.md",
		"71_tennis.ru.md",
		"72_tlckertape.ru.md",
		"73_tv_plot.ru.md",
		"74_twonky.ru.md",
		"75_two_to_ten.ru.md",
		"76_ufo.ru.md",
		"77_under_and_over.ru.md",
		"78_vangam.ru.md",
		"79_warflsh.ru.md",
		"80_word_search_puzzle.ru.md",
		"81_wumpus_1.ru.md",
		"82_wumpus_2.ru.md"
		]
		for file in rules_files:
			output_file:Path = Path( self.base_path / self.lang / 'rules' / file )
			output_file.parent.mkdir(parents=True, exist_ok=True)
			output_file.write_text('',encoding='UTF-8')






if __name__ == '__main__':
	langs_list:list = ['ru','he','en']
	
	for lang in langs_list:
		g = MoreBasicGames(lang)
		#g.create_rules_files()
		asyncio.run( g.generate_python_code())