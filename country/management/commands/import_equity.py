from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
import gspread
from country.models import Country, Tender, EquityCategory, EquityKeywords




class Command(BaseCommand):
    help = 'Import tender from google sheets url'

    def handle(self, *args, **kwargs):
        categories = ["Poverty","Unemployment","Prisoners / ex-prisoners","Homelessness","Disability","Gender,sexual orientation, sex",
                   "Ethnicity","Religion","Mental Health","Age","General","Migration"]
            
        
        for category in categories:
            obj , created = EquityCategory.objects.get_or_create(category_name=category)
            print(f'Created : {obj}')
        data = {"Poverty":[{"Moldova":["sărăcie","Bunăstare","Vulnerabilitate","Sărăcia tranzitorii","Social","drepturi","înzestrare","înzestrare",
                                       "nevoi de baza","бедность","Благополучие","уязвимость","кратковременная бедность","социальный","пособие",
                                       "пожертвование","основные потребности"],
                            "United Kingdom":["poverty","Well-Being","Vulnerability","Transient Poverty","Social","entitlements","endowments","basic needs"],
                            "Kenya":["poverty","Well-Being","Vulnerability","Transient Poverty","Social","entitlements","endowments","basic needs"],
                            "Mexico":["pobreza","Bienestar","Vulnerabilidad","La pobreza transitoria","Social","derechos","dotaciones","necesidades básicas"],
                            "Kyrgyz Republic":["жакырчылык","бакубатчылык","аялуу","убактылуу жакырчылык","социалдык","жөлөкпул","кайыр садага",
                                              "негизги муктаждыктар","бедность","Благополучие","уязвимость","кратковременная бедность","социальный","пособие",
                                              "пожертвование","основные потребности"]}],
                "Unemployment":[{"Moldova":["sărășomeri având","beneficii","Concediu","ocazional","Căutatori de slujbe","şomaj","без работы","пособие",
                                       "отпуск за свой счет","отпуск без сохранения заработной платы","временный рабочий","Ищущие работу","безработица"],
                            "United Kingdom":["unemploy","benefits","Furlough","Casual","Zero","Jobseekers","Worklessness"],
                            "Kenya":["unemploy","benefits","Furlough","Casual","Zero","Jobseekers","Worklessness"],
                            "Mexico":["pleo","beneficios","Permiso","Casual","Cero","Solicitantes de empleo","La falta de trabajo"],
                            "Kyrgyz Republic":["жумушсуз","жөлөкпул","өз эсебинен өргүү","төлөнбөгөн өргүү","убактылуу жумушчу","жумуш издегендер","жумушсуздук",
                                              "без работы","пособие","отпуск за свой счет","отпуск без сохранения заработной платы","временный рабочий","Ищущие работу","безработица"]}],
                "Prisoners / ex-prisoners":[{"Moldova":["prizonier","condamna","penal","заключённый / заключенный","осуждённый / осужденный","уголовник","преступник",],
                            "United Kingdom":["prisoner","convict","criminal"],
                            "Kenya":["prisoner","convict","criminal"],
                            "Mexico":["prisionero","condenar","delincuente"],
                            "Kyrgyz Republic":["камактагы адам","соттолгон адам","кылмышкер","заключённый / заключенный","осуждённый / осужденный","уголовник","преступник"]}],  
                "Homelessness":[{"Moldova":["Lipsa de adăpost","Fără adăpost","Cazare","Social","adăposturi","strămutate","Hotel","отсутствие постоянного места жительства","бездомный","содержание","расселение", "размещение","убежище (предоставление убежища)","жилье",
                                            "бомж","приют","социальный","приют","перемещенные","общежитие","Ночлег и завтрак","Гостиница"],
                            "United Kingdom":["Homelessness","Homeless","Housing","Accomodation","Rough Sleeping","Refuges","Social","Shelters","Displaced","Hostels","B&B","Hotel","Squat"],
                            "Kenya":["Homelessness","Homeless","Housing","Accomodation","Rough Sleeping","Refuges","Social","Shelters","Displaced","Hostels","B&B","Hotel","Squat"],
                            "Mexico":["La falta de vivienda","Vagabundo","Alojamiento","alojamiento","duermen en la calle","refugios","Social","refugios","Desplazado","hostales","cama y desayuno","Hotel","Ponerse en cuclillas"],
                            "Kyrgyz Republic":["үй-жайсыздык","туруктуу жашаган жердин жоктугу","үй-жайсыз","отурукташтыруу","жайгаштыруу","жайгаштыруу","баш калкалоочу жай берүү","турак-жай","жайгаштыруу","селсаяк","баш калкалоочу жай","социалдык","баш калкалоочу жай","которулгандар","жатакана","уктоочу жай жана эртең мененки тамактануу","мейманкана","үй-жайсыз адамдардын бош турган үй же батирди мыйзамсыз басып алуусу","бездномность","отсутствие постоянного места жительства","бездомный","содержание","расселение" ,"размещение","убежище (предоставление убежища)","жилье","Размещение","бомж","приют","социальный","приют","перемещенные","общежитие","Ночлег и завтрак","Гостиница","незаконное вселение в пустой дом или квартиру группы бездомных людей"]}],                                      
                "Disability":[{"Moldova":["incapacitate","dezactivat","orb","vedere","mobilitate","dexteritate manuala","dexteritate de învățare","problemă de sănătate mintală","depreciere de vorbire",
                                            "handicap cognitiv","epilepsie","cardiovascular","astm","cancer","anemie","инвалидность","человек с инвалидностью","слепой","зрение","мобильность","ловкость рук"
                                            ,"проблемы с психическим здоровьем","нарушение речи","когнитивная инвалидность","эпилепсия","сердечно-сосудистый","астма","рак","анемия"],
                            "United Kingdom":["disability","disabled","blind","sight","mobility","manual dexterity","learning dexterity","mental health concern" ,"speech impairment" ,"cognitive disability","epilepsy","cardiovascular","asthma","cancer","anaemia","motor neurone"],
                            "Kenya":["disability","disabled","blind","sight","mobility","manual dexterity","learning dexterity","mental health concern" ,"speech impairment" ,"cognitive disability","epilepsy","cardiovascular","asthma","cancer","anaemia","motor neurone"],
                            "Mexico":["discapacidad","discapacitado","ciego","visión","movilidad","destreza manual","la destreza de aprendizaje","preocupación de la salud mental","discapacidad del habla","discapacidad cognitiva","epilepsia","cardiovascular","asma","cáncer","anemia","neurona motora"],
                            "Kyrgyz Republic":["майыптуулук","майып","сокур","көздүн көрүсүү","мобилдүүлүк","колдун эптүүлүгү","окуу эптүүлүгү","психикалык саламаттык көйгөйлөрү","сүйлөө жөндөмүнүн бузулушу","когнитивдик майыптык","талма","Жүрөк-кан тамыр","астма","рак","аз кандуулук","инвалидность","человек с инвалидностью","слепой","зрение","мобильность","ловкость рук","проблемы с психическим здоровьем","нарушение речи","когнитивная инвалидность","эпилепсия","сердечно-сосудистый","астма","рак","анемия"]}],
                "Gender,sexual orientation, sex":[{"Moldova":["LGBT","lesbiană","homosexual","bisexuat","gen","transexual","schimbare de sex","gen neutru","Parteneriat civil","ЛГБТ","лесбиянка","гей","бисексуал","Пол","транссексуал","человек с нетрадиционной сексуальной ориентацией","изменение пола","гендерно нейтральный","гендерфлюидный","гендерквир" ,"спектр гендерных идентичностей, отличных от бинарного мужского и женского гендера","МСМ","мужчины, занимающиеся сексом с мужчинами","гетеросексуал","господин","госпожа","гопожа","бракб супружество","Гражданский брак"],
                            "United Kingdom":["LGBT","Lesbian","Gay","Bisexual" ,"gender","transexual","queer","feminis","gender reassignment" ,"gender neutral" ,"gender fluid" ,"gender queer","non-binary","hetrosexual","straight" ,"Mr","Mrs","Miss","Mx","Dame","Marriage","Civil Partnership"],
                            "Kenya":["LGBT","Lesbian","Gay","Bisexual" ,"gender","transexual","queer","feminis","gender reassignment" ,"gender neutral" ,"gender fluid" ,"gender queer","non-binary","hetrosexual","straight" ,"Mr","Mrs","Miss","Mx","Dame","Marriage","Civil Partnership"],
                            "Mexico":["LGBT","lesbiana","homosexual","Bisexual","género","transexual","extraño","Feminis","cambio de sexo","genero neutral","el fluido de género","GENDERQUEER","no binario","hetrosexual","Derecho","Señor","señora","Pierda","mx","Dama","Matrimonio","Unión civil"],
                            "Kyrgyz Republic":["ЛГБТ","лесбиянка","гей","бисексуал","жыныс","транссексуал","сексуалдык багыты салттуу эмес адам","жынысты алмаштыруу","гендердик нейтралдуу","гендерфлюиддүү","гендерквир","эркек менен эркек","эркектер менен жыныстык катнашка барган эркектер","гетеросексуал","мырза","айым","айым","никелешүү","жарандык нике","ЛГБТ","лесбиянка","гей","бисексуал","Пол","транссексуал","человек с нетрадиционной сексуальной ориентацией","изменение пола","гендерно нейтральный","гендерфлюидный","гендерквир" ,"спектр гендерных идентичностей, отличных от бинарного мужского и женского гендера","МСМ","мужчины, занимающиеся сексом с мужчинами","гетеросексуал","господин","госпожа","гопожа","бракб супружество","Гражданский брак"]}],
                "Ethnicity":[{"Moldova":["Etnie","minoritate etnică","rasă","Rasial","asiatic","Bangladesh","chinez","indian","pakistanez","asiatice altele","Negru african","Caraibe negru","Negru altele","Mixt Alb / Asiatic","Mixt Alb / Negru african","Mixt Alb / Negru Caraibe","mixte altele","alb britanic","alb irlandez","Alb Gypsy / Traveler","alte alb","Alte","arab","Oricare altul","Этнос","этническое меньшинство","раса","расовый","азиатская","бангладешец","Китаец","Индус","Пакистанец","другие из Азии"],
                            "United Kingdom":["BAME","Ethnicity","ethnic minority","race","Racial","Asian","Bangladeshi","Chinese","Indian","Pakistani","Asian other","Black African","Black Caribbean","Black other","Mixed White/Asian","Mixed White/Black African","Mixed White/Black Caribbean","Mixed other","White British","White Irish","White Gypsy/Traveller","White other","Other","Arab","Any other"],
                            "Kenya":["BAME","Ethnicity","ethnic minority","race","Racial","Asian","Bangladeshi","Chinese","Indian","Pakistani","Asian other","Black African","Black Caribbean","Black other","Mixed White/Asian","Mixed White/Black African","Mixed White/Black Caribbean","Mixed other","White British","White Irish","White Gypsy/Traveller","White other","Other","Arab","Any other"],
                            "Mexico":["BAME","etnicidad","Minoría étnica","raza","Racial","asiático","Bangladesh","chino","indio","pakistaní","Asiático","negro africano","negro del Caribe","negro otra","Blanco mezclado / asiático","Negro blanco africano mixta","Negro del Caribe blanco mezclado","otra mixta","British White","blanco irlandés","Blanco Gypsy / viajeros","blanco otro","Otro","árabe","Cualquier otro"],
                            "Kyrgyz Republic":["Этнос","этникалык азчылык","раса","расалык","азиялык","бангладеш","кытай","индиялык","пакистандык","азиялык, башка","кара, африкалык","кара, карибдик","кара, башка" ,"аралаш ак / азиялык","аралаш ак / кара африкалык","аралаш ак / кара карибдик","аралаш,  башка","ак британ","ак Irish","Ак Gypsy / саякатчы","ак башка","башка","араб","ар кандай башка","этническое меньшинство","раса","расовый","азиатская","бангладешец","Китаец","Индус","Пакистанец","другие из Азии"]}],  
                "Religion":[{"Moldova":["musulman","islamica","creştin","evreu","hinduism","Sikhism","catolic","protestant","baptist","metodist","мусульманин","исламский","Кристиан","иудей","индуизм","сикхизм","католик","протестант","баптист","методист"],
                            "United Kingdom":["Muslim","islamic","christian","jew","hinduism","Sikhism","catholic","protestant","baptist","methodist"],
                            "Kenya":["Muslim","islamic","christian","jew","hinduism","Sikhism","catholic","protestant","baptist","methodist"],
                            "Mexico":["musulmán","islámico","cristiano","judío","hinduismo","sijismo","católico","protestante","bautista","metodista"],
                            "Kyrgyz Republic":["мусулман","исламдык","христиан","иудей","индуизм","сикхизм","католик","протестанттык","баптист","методист","мусульманин","исламский","Кристиан","иудей","индуизм","сикхизм","католик","протестант","баптист","методист"]}],
                "Mental Health":[{"Moldova":["Mental","tulburare","Abuz","Dependenta de","anorexie","Asperger","Autism","Comportament","Bipolar","bulimia","Demenţă","depresiune","Dezvoltare","Epilepsie","sechestrare","Intelectual","Sănătate","Stres post traumatic","Psihoză","schizofrenie","Autoagresiune","stigmat","Sinucidere","TSPT","умственный","расстройство","Злоупотребление","Зависимость","Анорексия","Аспергера","аутизм","Поведение","биполярный","булимия","слабоумие","депрессия","развитие","эпилепсия","припадок","гиперкинетический","интеллектуальный","Здоровье","Посттравматическое стрессовое расстройство","Психоз","Шизофрения","Причинять себе вред","стигма","самоубийца","ПТСР"],
                            "United Kingdom":["Mental","disorder","Abuse","Addiction","Anorexia","Aspergers","Autism" ,"Behaviour","Bipolar","Bulimia","Dementia","Depression" ,"Development","Epilepsy","Seizure","Hyperkinetic","Intellectual","Health","Post Traumatic Stress Disorder","Psychosis","Schizophrenia","Self Harm","Stigma","Suicide","ptsd"],
                            "Kenya":["Mental","disorder","Abuse","Addiction","Anorexia","Aspergers","Autism" ,"Behaviour","Bipolar","Bulimia","Dementia","Depression" ,"Development","Epilepsy","Seizure","Hyperkinetic","Intellectual","Health","Post Traumatic Stress Disorder","Psychosis","Schizophrenia","Self Harm","Stigma","Suicide","ptsd"],
                            "Mexico":["Mental","trastorno","Abuso","Adiccion","Anorexia","Asperger","Autismo","Comportamiento","Bipolar","Bulimia","Demencia","Depresión","Desarrollo","Epilepsia","Incautación","hipercinético","Intelectual","Salud","Trastorno de estrés postraumático","Psicosis","Esquizofrenia","Autolesiones","Estigma","Suicidio","trastorno de estrés postraumático"],
                            "Kyrgyz Republic":["акыл","бузулгандык","кыянаттык","көзкарандык","анорексия","аспергер синдрому","аутизм","жүрүм-турум","биполярдуу","булимия","кем акылдык","депрессия","өнүгүү","эпилепсия","талма","гиперкинетикалык","интеллектуалдык","ден соолук","жаракат алгандан кийин келип чыгуучу стресстик бузулуу","психоз","шизофрения","өзүнө зыян келтирүү","стигма","өзүн өзү өлтүргөн киши","жаракат алгандан кийин келип чыгуучу стресстик бузулуу","умственный","расстройство","Злоупотребление","Зависимость","Анорексия","Аспергера","аутизм","Поведение","биполярный","булимия","слабоумие","депрессия","развитие","эпилепсия","припадок","гиперкинетический","интеллектуальный","Здоровье","Посттравматическое стрессовое расстройство","Психоз","Шизофрения","Причинять себе вред","стигма","самоубийца","ПТСР"]}],
                "Age":[{"Moldova":["Tineri","îngrijire rezidențială","paliativ","vârstnic","Sub 20","21-30","31-40","41-50","51-55","5660","61-65","66-70","71-75","75 +","молодой","Попечение по месту жительства","паллиативный","престарелые","Под 20"],
                            "United Kingdom":["Young","Residential Care","palliative","elderly","Under 20","21-30","31-40","41-50","51-55","56-60","61-65","66-70","71-75","75 +"],
                            "Kenya":["Young","Residential Care","palliative","elderly","Under 20","21-30","31-40","41-50","51-55","56-60","61-65","66-70","71-75","75 +"],
                            "Mexico":["Joven","Atención residencial","paliativo","mayor","Menos de 20"],
                            "Kyrgyz Republic":["молодой","Попечение по месту жительства","паллиативный","престарелые","Под 20","21-30","31-40","41-50","51-55","56-60","61-65","66-70","71-75","75 +","жаш","жашаган жери боюнча камкордукка алуу","паллиативдик","улгайгандар","20 жашка чейинкилер"]}],
                "General":[{"Moldova":["vulnerabil","dezavantajate","bunăstare","ingrijitor","graviditate","Maternitate","medicament","alcool","Vulnerabilitate","subnutriție","Robie","strămutate","уязвимый","неблагоприятный","лишенный","благосостояние","сиделка","беременность","материнство","препарат, средство, медикамент","алкоголь","уязвимость (уязвимый, слабый)","недоедание","Рабство","перемещенные"],
                            "United Kingdom":["Vulnerable","disadvantaged","deprive","welfare","carer","Pregnancy","Maternity","drug","alcohol","Vulnerability","Undernourishment","Slavery","Displaced"],
                            "Kenya":["Vulnerable","disadvantaged","deprive","welfare","carer","Pregnancy","Maternity","drug","alcohol","Vulnerability","Undernourishment","Slavery","Displaced"],
                            "Mexico":["Vulnerable","perjudicado","privar","bienestar","cuidador","El embarazo","Maternidad","droga","alcohol","Vulnerabilidad","Desnutrición","Esclavitud","Desplazado"],
                            "Kyrgyz Republic":["аялуу","жагымсыз","ажыраган","жетиштүүлүк","оорулууга баш-көз аял","кош бойлуулук","энелик","дары-дармек","алкоголь","алсыз","начар тамактануу","кулчулук","которулгандар","уязвимый","неблагоприятный","лишенный","благосостояние","сиделка","беременность","материнство","препарат, средство, медикамент","алкоголь","уязвимость (уязвимый, слабый)","недоедание","Рабство","перемещенные"]}],
                "Migration":[{"Moldova":["migrator","migrațiune","Refugiat","Azil","мигрант","миграция","беженец","убежище"],
                            "United Kingdom":["Migrant","Migration","Refugee","Asylum"],
                            "Kenya":["Migrant","Migration","Refugee","Asylum"],
                            "Mexico":["Inmigrante","Migración","Refugiado","Asilo"],
                            "Kyrgyz Republic":["мигрант","миграция","беженец","убежище","мигрант","миграция","качкын" ,"баш калкалоочу жай"]}],
                }

        print('Importingg!!!!!!!!')
        try:
            for keys,values in data.items():
                category = EquityCategory.objects.get(category_name=keys)
                for country in Country.objects.all():
                    items = values[0][country.name]
                    for item in items:
                        obj , created = EquityKeywords.objects.get_or_create(equity_category=category,country=country,keyword=item)
                        print(f'Created : {obj}')
        except Exception as e:
            print(e)

