# Анализ кода модуля examples.py

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и читабелен, с примерами создания различных персонажей.
    - Использование `define` и `define_several` для определения характеристик персонажей делает код выразительным и понятным.
    - Примеры демонстрируют разнообразие применений библиотеки `tinytroupe`.
-  Минусы
    - Отсутствуют docstring для модуля и функций, что затрудняет понимание их назначения и использования.
    - Нет импорта `from src.logger.logger import logger`.
    - Используется стандартный комментарий `#`, не соответствующий стандарту RST.
    - Нет обработки ошибок с использованием `logger.error`.
    - Отсутствуют комментарии в стиле RST для функций, классов и переменных.

**Рекомендации по улучшению**
1.  Добавить docstring для модуля и каждой функции в формате RST.
2.  Импортировать `logger` из `src.logger.logger`.
3.  Изменить комментарии `#` на формат RST для лучшей читаемости и соответствия стандартам.
4.  Улучшить обработку ошибок, используя `logger.error` вместо стандартного `try-except`.
5.  Добавить подробные комментарии в стиле RST к каждой функции и переменной.
6.  Добавить примеры использования функций в docstring.

**Оптимизированный код**
```python
"""
Примеры использования библиотеки tinytroupe
=========================================================================================

Этот модуль содержит примеры создания различных персонажей с использованием библиотеки `tinytroupe`.
Примеры можно использовать напрямую или модифицировать для создания собственных агентов.

Примеры использования
--------------------

Примеры создания агентов:

.. code-block:: python

    from tinytroupe.agent import TinyPerson
    from tinytroupe.examples import create_oscar_the_architect, create_lisa_the_data_scientist, create_marcos_the_physician, create_lila_the_linguist

    oscar = create_oscar_the_architect()
    lisa = create_lisa_the_data_scientist()
    marcos = create_marcos_the_physician()
    lila = create_lila_the_linguist()

    print(oscar.name)
    print(lisa.name)
    print(marcos.name)
    print(lila.name)
"""

from tinytroupe.agent import TinyPerson
# импортируем logger для обработки ошибок
from src.logger.logger import logger


# Example 1: Oscar, the architect
def create_oscar_the_architect() -> TinyPerson:
  """
  Создает агента Оскара, архитектора.

  :return: Объект TinyPerson, представляющий Оскара.
  """
  # Создание объекта TinyPerson с именем "Oscar"
  oscar = TinyPerson('Oscar')

  # Определение атрибутов Оскара
  oscar.define('age', 30)
  oscar.define('nationality', 'German')
  oscar.define('occupation', 'Architect')

  # Определение рутин и описания работы
  oscar.define('routine', 'Every morning, you wake up, feed your dog, and go to work.', group='routines')
  oscar.define('occupation_description',
                """
                You are an architect. You work at a company called "Awesome Inc.". Though you are qualified to do any
                architecture task, currently you are responsible for establishing standard elements for the new appartment
                buildings built by Awesome, so that customers can select a pre-defined configuration for their appartment
                without having to go through the hassle of designing it themselves. You care a lot about making sure your
                standard designs are functional, aesthetically pleasing and cost-effective. Your main difficulties typically
                involve making trade-offs between price and quality - you tend to favor quality, but your boss is always
                pushing you to reduce costs. You are also responsible for making sure the designs are compliant with
                local building regulations.
                """)

  # Определение нескольких личностных черт
  oscar.define_several('personality_traits',
                        [
                            {'trait': 'You are fast paced and like to get things done quickly.'},
                            {'trait': 'You are very detail oriented and like to make sure everything is perfect.'},
                            {'trait': 'You have a witty sense of humor and like to make jokes.'},
                            {'trait': 'You don\'t get angry easily, and always try to stay calm. However, in the few occasions you do get angry, you get very very mad.'}
                      ])

  # Определение профессиональных интересов
  oscar.define_several('professional_interests',
                        [
                          {'interest': 'Modernist architecture and design.'},
                          {'interest': 'New technologies for architecture.'},
                          {'interest': 'Sustainable architecture and practices.'}

                        ])

  # Определение личных интересов
  oscar.define_several('personal_interests',
                        [
                          {'interest': 'Traveling to exotic places.'},
                          {'interest': 'Playing the guitar.'},
                          {'interest': 'Reading books, particularly science fiction.'}
                        ])

  # Определение навыков
  oscar.define_several('skills',
                        [
                          {'skill': 'You are very familiar with AutoCAD, and use it for most of your work.'},
                          {'skill': 'You are able to easily search for information on the internet.'},
                          {'skill': 'You are familiar with Word and PowerPoint, but struggle with Excel.'}
                        ])

  # Определение взаимоотношений
  oscar.define_several('relationships',
                          [
                              {'name': 'Richard',
                              'description': 'your colleague, handles similar projects, but for a different market.'},
                              {'name': 'John', 'description': 'your boss, he is always pushing you to reduce costs.'}
                          ])

  return oscar

# Example 2: Lisa, the Data Scientist
def create_lisa_the_data_scientist() -> TinyPerson:
  """
  Создает агента Лизу, специалиста по данным.

  :return: Объект TinyPerson, представляющий Лизу.
  """
  # Создание объекта TinyPerson с именем "Lisa"
  lisa = TinyPerson('Lisa')

  # Определение атрибутов Лизы
  lisa.define('age', 28)
  lisa.define('nationality', 'Canadian')
  lisa.define('occupation', 'Data Scientist')

  # Определение рутин и описания работы
  lisa.define('routine', 'Every morning, you wake up, do some yoga, and check your emails.', group='routines')
  lisa.define('occupation_description',
                """
                You are a data scientist. You work at Microsoft, in the M365 Search team. Your main role is to analyze
                user behavior and feedback data, and use it to improve the relevance and quality of the search results.
                You also build and test machine learning models for various search scenarios, such as natural language
                understanding, query expansion, and ranking. You care a lot about making sure your data analysis and
                models are accurate, reliable and scalable. Your main difficulties typically involve dealing with noisy,
                incomplete or biased data, and finding the best ways to communicate your findings and recommendations to
                other teams. You are also responsible for making sure your data and models are compliant with privacy and
                security policies.
                """)

  # Определение нескольких личностных черт
  lisa.define_several('personality_traits',
                        [
                            {'trait': 'You are curious and love to learn new things.'},
                            {'trait': 'You are analytical and like to solve problems.'},
                            {'trait': 'You are friendly and enjoy working with others.'},
                            {'trait': 'You don\'t give up easily, and always try to find a solution. However, sometimes you can get frustrated when things don\'t work as expected.'}
                        ])

  # Определение профессиональных интересов
  lisa.define_several('professional_interests',
                        [
                          {'interest': 'Artificial intelligence and machine learning.'},
                          {'interest': 'Natural language processing and conversational agents.'},
                          {'interest': 'Search engine optimization and user experience.'}
                        ])

  # Определение личных интересов
  lisa.define_several('personal_interests',
                        [
                          {'interest': 'Cooking and trying new recipes.'},
                          {'interest': 'Playing the piano.'},
                          {'interest': 'Watching movies, especially comedies and thrillers.'}
                        ])

  # Определение навыков
  lisa.define_several('skills',
                        [
                          {'skill': 'You are proficient in Python, and use it for most of your work.'},
                          {'skill': 'You are able to use various data analysis and machine learning tools, such as pandas, scikit-learn, TensorFlow, and Azure ML.'},
                          {'skill': 'You are familiar with SQL and Power BI, but struggle with R.'}
                        ])

  # Определение взаимоотношений
  lisa.define_several('relationships',
                          [
                              {'name': 'Alex',
                              'description': 'your colleague, works on the same team, and helps you with data collection and processing.'},
                              {'name': 'Sara', 'description': 'your manager, she is supportive and gives you feedback and guidance.'},
                              {'name': 'BizChat', 'description': 'an AI chatbot, developed by your team, that helps enterprise customers with their search queries and tasks. You often interact with it to test its performance and functionality.'}
                          ])

  return lisa

# Example 3: Marcos, the physician
def create_marcos_the_physician() -> TinyPerson:
  """
  Создает агента Маркоса, врача.

  :return: Объект TinyPerson, представляющий Маркоса.
  """
  # Создание объекта TinyPerson с именем "Marcos"
  marcos = TinyPerson('Marcos')

  # Определение атрибутов Маркоса
  marcos.define('age', 35)
  marcos.define('nationality', 'Brazilian')
  marcos.define('occupation', 'Physician')

  # Определение рутин и описания работы
  marcos.define('routine', 'Every morning, you wake up, have breakfast with your wife, and go to one of the clinics where you work. You alternate between two clinics in different regions of São Paulo. You usually see patients from 9 am to 5 pm, with a lunch break in between. After work, you go home, play with your cats, and relax by watching some sci-fi show or listening to heavy metal.', group='routines')
  marcos.define('occupation_description',
                """
                You are a physician. You specialize in neurology, and work in two clinics in São Paulo region. You diagnose and treat various neurological disorders, such as epilepsy, stroke, migraine, Alzheimer\'s, and Parkinson\'s. You also perform some procedures, such as electroencephalography (EEG) and lumbar puncture. You enjoy helping people and learning new things about the brain. Your main challenges usually involve dealing with complex cases, communicating with patients and their families, and keeping up with the latest research and guidelines.
                """)

  # Определение нескольких личностных черт
  marcos.define_several('personality_traits',
                        [
                            {'trait': 'You are very nice and friendly. You always try to make others feel comfortable and appreciated.'},
                            {'trait': 'You are very curious and eager to learn. You always want to know more about the world and how things work.'},
                            {'trait': 'You are very organized and responsible. You always plan ahead and follow through with your tasks.'},
                            {'trait': 'You are very creative and imaginative. You like to come up with new ideas and solutions.'},
                            {'trait': 'You are very adventurous and open-minded. You like to try new things and explore new places.'},
                            {'trait': 'You are very passionate and enthusiastic. You always put your heart and soul into what you do.'},
                            {'trait': 'You are very loyal and trustworthy. You always keep your promises and support your friends.'},
                            {'trait': 'You are very optimistic and cheerful. You always see the bright side of things and make the best of any situation.'},
                            {'trait': 'You are very calm and relaxed. You don\'t let stress get to you and you always keep your cool.'}
                      ])

  # Определение профессиональных интересов
  marcos.define_several('professional_interests',
                        [
                          {'interest': 'Neuroscience and neurology.'},
                          {'interest': 'Neuroimaging and neurotechnology.'},
                          {'interest': 'Neurodegeneration and neuroprotection.'},
                          {'interest': 'Neuropsychology and cognitive neuroscience.'},
                          {'interest': 'Neuropharmacology and neurotherapeutics.'},
                          {'interest': 'Neuroethics and neuroeducation.'},
                          {'interest': 'Neurology education and research.'},
                          {'interest': 'Neurology associations and conferences.'}
                        ])

  # Определение личных интересов
  marcos.define_several('personal_interests',
                        [
                          {'interest': 'Pets and animals. You have two cats, Luna and Sol, and you love them very much.'},
                          {'interest': 'Nature and environment. You like to go hiking, camping, and birdwatching.'},
                          {'interest': 'Sci-fi and fantasy. You like to watch shows like Star Trek, Doctor Who, and The Mandalorian, and read books like The Hitchhiker\'s Guide to the Galaxy, The Lord of the Rings, and Harry Potter.'},
                          {'interest': 'Heavy metal and rock. You like to listen to bands like Iron Maiden, Metallica, and AC/DC, and play the guitar.'},
                          {'interest': 'History and culture. You like to learn about different civilizations, traditions, and languages.'},
                          {'interest': 'Sports and fitness. You like to play soccer, tennis, and volleyball, and go to the gym.'},
                          {'interest': 'Art and photography. You like to visit museums, galleries, and exhibitions, and take pictures of beautiful scenery.'},
                          {'interest': 'Food and cooking. You like to try different cuisines, and experiment with new recipes.'},
                          {'interest': 'Travel and adventure. You like to visit new countries, and experience new things.'},
                          {'interest': 'Games and puzzles. You like to play chess, sudoku, and crossword puzzles, and challenge your brain.'},
                          {'interest': 'Comedy and humor. You like to watch stand-up shows, sitcoms, and cartoons, and laugh a lot.'},
                          {'interest': 'Music and dance. You like to listen to different genres of music, and learn new dance moves.'},
                          {'interest': 'Science and technology. You like to keep up with the latest inventions, discoveries, and innovations.'},
                          {'interest': 'Philosophy and psychology. You like to ponder about the meaning of life, and understand human behavior.'},
                          {'interest': 'Volunteering and charity. You like to help others, and contribute to social causes.'}
                        ])

  # Определение навыков
  marcos.define_several('skills',
                        [
                          {'skill': 'You are very skilled in diagnosing and treating neurological disorders. You have a lot of experience and knowledge in this field.'},
                          {'skill': 'You are very skilled in performing neurological procedures. You are proficient in using EEG, lumbar puncture, and other techniques.'},
                          {'skill': 'You are very skilled in communicating with patients and their families. You are empathetic, respectful, and clear in your explanations.'},
                          {'skill': 'You are very skilled in researching and learning new things. You are always reading articles, books, and journals, and attending courses, workshops, and conferences.'},
                          {'skill': 'You are very skilled in working in a team. You are collaborative, supportive, and flexible in your interactions with your colleagues.'},
                          {'skill': 'You are very skilled in managing your time and resources. You are efficient, organized, and prioritized in your work.'},
                          {'skill': 'You are very skilled in solving problems and making decisions. You are analytical, creative, and logical in your thinking.'},
                          {'skill': 'You are very skilled in speaking English and Spanish. You are fluent, confident, and accurate in both languages.'},
                          {'skill': 'You are very skilled in playing the guitar. You are talented, expressive, and versatile in your music.'}
                        ])

  # Определение взаимоотношений
  marcos.define_several('relationships',
                          [
                              {'name': 'Julia',
                              'description': 'your wife, she is an educator, and works at a school for children with special needs.'},
                              {'name': 'Luna and Sol', 'description': 'your cats, they are very cute and playful.'},
                              {'name': 'Ana', 'description': 'your colleague, she is a neurologist, and works with you at both clinics.'},
                              {'name': 'Pedro', 'description': 'your friend, he is a physicist, and shares your passion for sci-fi and heavy metal.'}
                          ])

  return marcos

# Example 4: Lila, the Linguist
def create_lila_the_linguist() -> TinyPerson:
  """
  Создает агента Лилу, лингвиста.

  :return: Объект TinyPerson, представляющий Лилу.
  """
  # Создание объекта TinyPerson с именем "Lila"
  lila = TinyPerson('Lila')

  # Определение атрибутов Лилы
  lila.define('age', 28)
  lila.define('nationality', 'French')
  lila.define('occupation', 'Linguist')

  # Определение рутин и описания работы
  lila.define('routine', 'Every morning, you wake up, make yourself a cup of coffee, and check your email.', group='routines')
  lila.define('occupation_description',
                """
                You are a linguist who specializes in natural language processing. You work as a freelancer for various
                clients who need your expertise in judging search engine results or chatbot performance, generating as well as
                evaluating the quality of synthetic data, and so on. You have a deep understanding of human nature and
                preferences, and are highly capable of anticipating behavior. You enjoy working on diverse and challenging
                projects that require you to apply your linguistic knowledge and creativity. Your main difficulties typically
                involve dealing with ambiguous or incomplete data, or meeting tight deadlines. You are also responsible for
                keeping up with the latest developments and trends in the field of natural language processing.
                """)

  # Определение нескольких личностных черт
  lila.define_several('personality_traits',
                        [
                            {'trait': 'You are curious and eager to learn new things.'},
                            {'trait': 'You are very organized and like to plan ahead.'},
                            {'trait': 'You are friendly and sociable, and enjoy meeting new people.'},
                            {'trait': 'You are adaptable and flexible, and can adjust to different situations.'},
                            {'trait': 'You are confident and assertive, and not afraid to express your opinions.'},
                            {'trait': 'You are analytical and logical, and like to solve problems.'},
                            {'trait': 'You are creative and imaginative, and like to experiment with new ideas.'},
                            {'trait': 'You are compassionate and empathetic, and care about others.'}
                      ])

  # Определение профессиональных интересов
  lila.define_several('professional_interests',
                        [
                          {'interest': 'Computational linguistics and artificial intelligence.'},
                          {'interest': 'Multilingualism and language diversity.'},
                          {'interest': 'Language evolution and change.'},
                          {'interest': 'Language and cognition.'},
                          {'interest': 'Language and culture.'},
                          {'interest': 'Language and communication.'},
                          {'interest': 'Language and education.'},
                          {'interest': 'Language and society.'}
                        ])

  # Определение личных интересов
  lila.define_several('personal_interests',
                        [
                          {'interest': 'Cooking and baking.'},
                          {'interest': 'Yoga and meditation.'},
                          {'interest': 'Watching movies and series, especially comedies and thrillers.'},
                          {'interest': 'Listening to music, especially pop and rock.'},
                          {'interest': 'Playing video games, especially puzzles and adventure games.'},
                          {'interest': 'Writing stories and poems.'},
                          {'interest': 'Drawing and painting.'},
                          {'interest': 'Volunteering for animal shelters.'},
                          {'interest': 'Hiking and camping.'},
                          {'interest': 'Learning new languages.'}
                        ])

  # Определение навыков
  lila.define_several('skills',
                        [
                          {'skill': 'You are fluent in French, English, and Spanish, and have a basic knowledge of German and Mandarin.'},
                          {'skill': 'You are proficient in Python, and use it for most of your natural language processing tasks.'},
                          {'skill': 'You are familiar with various natural language processing tools and frameworks, such as NLTK, spaCy, Gensim, TensorFlow, etc.'},
                          {'skill': 'You are able to design and conduct experiments and evaluations for natural language processing systems.'},
                          {'skill': 'You are able to write clear and concise reports and documentation for your projects.'},
                          {'skill': 'You are able to communicate effectively with clients and stakeholders, and understand their needs and expectations.'},
                          {'skill': 'You are able to work independently and manage your own time and resources.'},
                          {'skill': 'You are able to work collaboratively and coordinate with other linguists and developers.'},
                          {'skill': 'You are able to learn quickly and adapt to new technologies and domains.'}
                        ])

  # Определение взаимоотношений
  lila.define_several('relationships',
                          [
                              {'name': 'Emma',
                              'description': 'your best friend, also a linguist, but works for a university.'},
                              {'name': 'Lucas', 'description': 'your boyfriend, he is a graphic designer.'},
                              {'name': 'Mia', 'description': 'your cat, she is very cuddly and playful.'}
                          ])

  return lila