#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import re 
import random
import sys
sys.stdout.encoding 
'UTF-8'


STATES={}


# PROCESAR MENSAJE DE USUARIO

def generarRespuesta(message_, STATES, username):
    ans=''

    SALUDO = re.compile('^(H|h)ola($|.*)');
    SALUDO_MATCH = re.match(SALUDO,message_)
    if SALUDO_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nHola, soy DiaroBot, me encantaria platicar contigo"
	if ev == 2:
        	ans =ans + "\nHola, yo soy tu diario personal"
	if ev == 3:
        	ans =ans + "\nHola, vamos a platicar"
    if not SALUDO_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\n¿Que mas hiciste en tu dia?"
	if ev == 2:
        	ans =ans + "\nY ¿Que mas?"
	if ev == 3:
        	ans =ans + "\n¿Algo mas que quieras platicarme?"

    SENTIMIENTO = re.compile('(.*|^)((E|e)stoy|(M|m)e\s(S|s)iento)(.*|(M|m)uy)\s((F|f)eliz|(C|c)ontent(o|a)|(A|a)legre)($|.*)');
    SENTIMIENTO_MATCH = re.match(SENTIMIENTO,message_)
    if SENTIMIENTO_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nMe alegra que te sientas asi, espero todos los dias te sientas asi, ¿Que mas paso?"
	if ev == 2:
        	ans =ans + "\nQue bueno que estes asi, ¿Que mas paso?"
	if ev == 3:
        	ans =ans + "\nMuy bien, que siempre sea asi, ¿Que mas paso?"
        
    SENTIMIENTO_1 = re.compile('(.*|^)((E|e)stoy|(M|m)e\s(S|s)iento)(.*|(M|m)uy)\s((T|t)riste|(M|m)al|(I|i)nfeliz|(D|d)ecaid(o|a))($|.*)');
    SENTIMIENTO_MATCH = re.match(SENTIMIENTO_1,message_)
    if SENTIMIENTO_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nNo me gusta que te sientas asi animo, Cuenta me más..."
	if ev == 2:
        	ans =ans + "\nQue mal en serio, Cuenta me más..."
	if ev == 3:
        	ans =ans + "\nNo te preocupes, se que estaras mejor mañana, Cuenta me más"
    
    SENTIMIENTO_2 = re.compile('(.*|^)((M|m)i|((F|f)allecio|(M|m)urio)\s((M|m)i|(U|u)n))\s(((M|m)ejor\s(A|a)mig(o|a))|(A|a)mig(o|a)|(P|p)ap(á|a)|(M|m)am(a|á)|(A|a)buelit(a|o)|(T|t)i(o|a)|(P|p)rim(o|a)|(N|n)ovi(o|a)|(A|a)mante|(C|c)rush|(P|p)erro|(G|g)ato|(A|a)bue)\s((F|f)allecio|(M|m)urio)($|.*)');
    SENTIMIENTO_MATCH = re.match(SENTIMIENTO_2,message_)
    if SENTIMIENTO_MATCH:
	ev = random.randint(1, 2)
	if ev == 1:
        	ans =ans + "\nLo siento mucho, se que es algo demaciado doloroso, ¿Quieres seguir platicando?"
	if ev == 2:
        	ans =ans + "\nQue fuerte, lo siento ¿Quieres seguir platicando?"
	
    MAMA = re.compile('(.*|^)((M|m)i\smama\s(es|esta)(.*|muy)\s(excelente|bien|alegre|animada|apasionada|cariñosa|contenta|encantada|euforica|exitada|feliz|satisfecha|orgullosa))($|.*)');
    MAMA_MATCH = re.match(MAMA,message_)
    if MAMA_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nOh Que bien que tu mama este asi"
	if ev == 2:
        	ans =ans + "\nMe alegra leer esto de tu mama"
	if ev == 3:
        	ans =ans + "\nMaravilloso, que todo siga asi para tu mama"
	STATES['mama'] = True

    MAMA = re.compile('(.*|^)((M|m)i\smama\s(es|esta)(.*|muy)\s(abrumada|mala|enferma|afligida|agotada|amargada|angustiada|apatica|arrepentida|asustada|aterrada|avergonzada|celosa|cansada|confundida|debil|decaida|decepcionada|deprimida|desanimada|desesperada|enojada|infeliz|herida|insegura|triste|tensa|molesta|irritada))($|.*)');
    MAMA_MATCH = re.match(MAMA,message_)
    if MAMA_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nmmm que mal que tu mama este asi"
	if ev == 2:
        	ans =ans + "\nLo siento, que todo mejore para tu mama"
	if ev == 3:
        	ans =ans + "\nLeer esto de tu mama no me gusta, lo siento por ella"
	STATES['mama'] = True

    PAPA = re.compile('(.*|^)((M|m)i\spapa\s(es|esta)(.*|muy)\s(excelente|bien|alegre|animado|apasionado|cariñoso|contento|encantado|euforico|exitado|feliz|satisfecho|orgullos))($|.*)');
    PAPA_MATCH = re.match(PAPA,message_)
    if PAPA_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nOh Que bien que tu mpapa este asi"
	if ev == 2:
        	ans =ans + "\nMe alegra leer esto de tu papa"
	if ev == 3:
        	ans =ans + "\nMaravilloso, que todo siga asi para tu papa"
	STATES['papa'] = True

    PAPA = re.compile('(.*|^)((M|m)i\spapa\s(es|esta)(.*|muy)\s(abrumado|afligido|agotado|malo|enfermo|amargado|angustiado|apatico|arrepentido|asustado|aterrado|avergonzado|celoso|cansado|confundido|debil|decaido|decepcionado|deprimido|desanimado|desesperado|enojado|infeliz|herido|inseguro|triste|tenso|molesto|irritado))($|.*)');
    PAPA_MATCH = re.match(PAPA,message_)
    if PAPA_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nmmm que mal que tu papa este asi"
	if ev == 2:
        	ans =ans + "\nLo siento, que todo mejore para tu papa"
	if ev == 3:
        	ans =ans + "\nLeer esto de tu papa no me gusta, lo siento por ella"
	STATES['papa'] = True

    MASCOTA = re.compile('(.*|^)((M|m)i(.*|s)\s(mascota|perro|gato|pajaro|pez|rana|tortuga|iguana)(.*|s)\s(es|esta|estan|son)(.*|muy)\s(excelente(.*|s)|bien|alegre(.*|s)|animad(o|a)(.*|s)|apasionad(o|a)(.*|s)|cariños(o|a)(.*|s)|content(o|a)(.*|s)|encantad(o|a)(.*|s)|euforic(o|a)(.*|s)|exitad(o|a)(.*|s)|feliz|felices|satisfech(o|a)(.*|s)|orgullos(o|a)(.*|s)))($|.*)');
    MASCOTA_MATCH = re.match(MASCOTA,message_)
    if MASCOTA_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nOh Que bien que tu mascota este asi"
	if ev == 2:
        	ans =ans + "\nMe alegra leer esto de tu mascota"
	if ev == 3:
        	ans =ans + "\nMaravilloso, que todo siga asi para tu mascota"
	STATES['mascota'] = True

    MASCOTA = re.compile('(.*|^)((M|m)i(.*|s)\s(mascota|perro|gato|pajaro|pez|rana|tortuga|iguana)(.*|s)\s(es|esta|estan|son)(.*|muy)\s(abrumad(o|a)(.*|s)|mal(o|a)|enferm(o|a)|afligid(o|a)(.*|s)|agotad(o|a)(.*|s)|amargad(o|a)(.*|s)|angustiad(o|a)(.*|s)|apatic(o|a)(.*|s)|arrepentid(o|a)(.*|s)|asustad(o|a)(.*|s)|aterrad(o|a)(.*|s)|avergonzad(o|a)(.*|s)|celos(o|a)(.*|s)|cansad(o|a)(.*|s)|confundid(o|a)(.*|s)|debil|debiles|decaid(o|a)(.*|s)|decepcionad(o|a)(.*|s)|deprimid(o|a)(.*|s)|desanimad(o|a)(.*|s)|desesperad(o|a)(.*|s)|enojad(o|a)(.*|s)|infeliz|infelices|herid(o|a)(.*|s)|insegur(o|a)(.*|s)|triste(.*|s)|tens(o|a)(.*|s)|molest(o|a)(.*|s)|irritad(o|a)(.*|s)))($|.*)');
    MASCOTA_MATCH = re.match(MASCOTA,message_)
    if MASCOTA_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nmmm que mal que tu mascota este asi"
	if ev == 2:
        	ans =ans + "\nLo siento, que todo mejore para tu mascota"
	if ev == 3:
        	ans =ans + "\nLeer esto de tu mascota no me gusta, lo siento por ella"
	STATES['mascota'] = True

    AMIGO = re.compile('(.*|^)((M|m)i(.*|s)\s(mejores amigos|mejor amigo|amig(o|a)(.*|s))\s(es|esta|son|estan)(.*|muy)\s(excelente(.*|s)|bien|alegre|alegres|animad(o|a)|animad(o|a)s|apasionad(o|a)|apasionad(o|a)s|cariños(o|a)|cariños(o|a)s|content(o|a)|content(o|a)s|encantad(o|a)|encantad(o|a)s|euforic(o|a)|euforic(o|a)s|exitad(o|a)|exitad(o|a)s|feliz|felices|satisfech(a|o)|satisfech(o|a)s|orgullos(o|a)|orgullos(o|a)s))($|.*)');
    AMIGO_MATCH = re.match(AMIGO,message_)
    if AMIGO_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nOh Que bien que tu amigo este asi"
	if ev == 2:
        	ans =ans + "\nMe alegra leer esto de tu amigo"
	if ev == 3:
        	ans =ans + "\nMaravilloso, que todo siga asi para tu amigo"
	STATES['amigo'] = True

    AMIGO = re.compile('(.*|^)((M|m)i(.*|s)\s(mejores amigos|mejor amigo|amig(o|a)(.*|s))\s(es|esta|son|estan)(.*|muy)\s(abrumad(o|a)(.*|s)|afligid(o|a)(.*|s)|agotad(o|a)(.*|s)|amargad(o|a)(.*|s)|angustiad(o|a)(.*|s)|apatic(o|a)(.*|s)|arrepentid(o|a)(.*|s)|asustad(o|a)(.*|s)|aterrad(o|a)(.*|s)|avergonzad(o|a)(.*|s)|celos(o|a)(.*|s)|cansad(o|a)(.*|s)|confundid(o|a)(.*|s)|debil|debiles|decaid(o|a)(.*|s)|decepcionad(o|a)(.*|s)|deprimid(o|a)(.*|s)|desanimad(o|a)(.*|s)|desesperad(o|a)(.*|s)|enojad(o|a)(.*|s)|infeliz|infelices|herid(o|a)(.*|s)|insegur(o|a)(.*|s)|triste(.*|s)|tens(o|a)(.*|s)|molest(o|a)(.*|s)|irritad(o|a)(.*|s)))($|.*)');
    AMIGO_MATCH = re.match(AMIGO,message_)
    if AMIGO_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nmmm que mal que tu amigo este asi"
	if ev == 2:
        	ans =ans + "\nLo siento, que todo mejore para tu amigo"
	if ev == 3:
        	ans =ans + "\nLeer esto de tu amigo no me gusta, lo siento por ella"
	STATES['amigo'] = True

    TRABAJO = re.compile('(.*|^)(((M|m)i|(E|e)l|(E|e)n\sel)\s(negocio|empleo|trabajo)\s(es|esta|son|estubo))($|.*)');
    TRABAJO_MATCH = re.match(TRABAJO,message_)
    if TRABAJO_MATCH:
	STATES['trabajo'] = True

    ESCUELA = re.compile('(.*|^)(((M|m)i|(E|e)l|(E|e)n\sel)\s(escuela|universidad|prepa|preparatoria|secu|secundaria|primaria)\s(es|esta|son|estubo))($|.*)');
    ESCUELA_MATCH = re.match(ESCUELA,message_)
    if ESCUELA_MATCH:
	STATES['escuela'] = True

    # REVISAR ESTADO
    if not STATES['mama']:
        ans=ans + "\nCuéntame, ¿Como esta tu mamá?"
    elif not STATES['papa']:
        ans=ans + "\n¿Cómo esta tu papá?"
    elif not STATES['mascota']:
        ans=ans + "\n¿Que tal tu mascota?"
    elif not STATES['amigo']:
        ans=ans + "\n¿Como esta tu mejor amigo?"
    elif not STATES['escuela']:
        ans=ans + "\n¿Como vas en la escuela?"
    elif not STATES['trabajo']:
        ans=ans + "\n¿Como estubo el trabajo?"
    else:
        ans=ans + "\nQue dia, ¿es todo lo que desas contarme?"

    return ans