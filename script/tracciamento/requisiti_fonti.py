#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name: requisiti-fonti.py
# Author: Tesser Paolo
# Date: 2015-03-17
# Mail: p.tesser921@gmail.com
# Modify
# Version   Date        Author          Description
# =======================================================================
# 0.0.1     2015-03-17  Tesser Paolo    codifica script
# -----------------------------------------------------------------------
# 0.0.2     2015-03-18  Tesser Paolo    terminato script con scrittura tracciamento su documento requisiti-fonti.tex
# -----------------------------------------------------------------------
# 0.0.3     2015-04-15  Tesser Paolo    aggiunto metodo per generare in un file tex, la lista dei requisiti
# -----------------------------------------------------------------------
#
__author__ = 'ptesser'
import re


class RequisitiFonti():

    __req_doc_path_str = ""
    __comp_doc_path_str = ""
    __write_doc_path_str = ""
    __write_list_req_str = ""

    __req_doc_file = ""
    __comp_doc_file = ""
    __write_doc_file = ""
    __write_list_req_file = ""

    __req_file_line = []
    __comp_file_line = []
    # array di soli requisiti per poterli scorrere dal primo all'ultimo nell'ordine di inserimento
    __req_fonti_array = []

    # dizionario per fare il tracciamento inverso fonti-requisiti
    __fonti_req_dict = {}
    # dizionario per ricavarmi le fonti sapendo il requisito come chiave
    __req_fonti_dict = {}
    # dizionario per ricavarmi i componenti sapendo il requisito come chiave
    __req_comp_dict = {}

    def __init__(self):
        pass

    def open_doc_req(self):
        self.__req_doc_path_str = "../../documenti/analisi_dei_requisiti/content/requisiti.tex"
        self.__req_doc_file = open(self.__req_doc_path_str, "r")
        self.__req_file_line = [line.strip() for line in self.__req_doc_file]
        # mi salvo tutte le righe del file in una lista togliendoli il carattere di ritorno a capo
        self.__req_doc_file.close()

    def open_doc_componenti(self):
        self.__comp_doc_path_str = "../../documenti/specifica_tecnica/content/tracciamento/componenti-requisiti.tex"
        self.__comp_doc_file = open(self.__comp_doc_path_str, "r")
        self.__comp_file_line = [line.strip() for line in self.__comp_doc_file]
        # mi salvo tutte le righe del file in una lista togliendoli il carattere di ritorno a capo
        self.__comp_doc_file.close()

    def take_req(self):
        for line in self.__req_file_line:
            req_match_re = re.match(r"^R(.*)", line)
            if req_match_re is not None:
                req = re.search(r"^R(.*?)\s", line)
                if req:
                    fonti_for_req_array = line.split('&')[2].strip()
                    fonti_single_array = fonti_for_req_array[:-2].strip().split("\\newline")
                    # aggiorno il dizionario con il nuovo valore del requisito e le sue fonti
                    self.__req_fonti_dict.update({req.group(): fonti_for_req_array})
                    # aggiorno l'array solo dei requisiti
                    self.__req_fonti_array.append(req.group())

                    for fonte in fonti_single_array:
                        if fonte.strip() in self.__fonti_req_dict:
                            self.__fonti_req_dict[fonte.strip()].append(req.group().strip())
                        else:
                            self.__fonti_req_dict[fonte.strip()] = [req.group().strip()]

    def take_req_comp(self):
        for line in self.__comp_file_line:
            comp_match_re = re.match(r"^(server|client)", line)
            if comp_match_re is not None:
                comp = re.search(r"^(server|client)(.*)&", line)
                comp = (comp.group(1) + comp.group(2)).strip()

                if comp:
                    # TODO: change name
                    fonti_for_req_array = line.split('&')[1].strip()
                    fonti_single_array = fonti_for_req_array[:-2].strip().split("\\newline")
                    for req in fonti_single_array:
                        if req.strip() in self.__req_comp_dict:
                            self.__req_comp_dict[req.strip()].append(comp.strip())
                        else:
                            self.__req_comp_dict[req.strip()] = [comp.strip()]

        # print self.__req_comp_dict

    def get_list_req(self):
        return self.__req_fonti_dict

    def get_list_fonti(self):
        return self.__fonti_req_dict

    def write_req_fonti(self):
        self.__write_doc_path_str = "requisiti-fonti.tex"
        self.__write_doc_file = open(self.__write_doc_path_str, "w")
        self.__write_doc_file.write("\subsection{Requisiti-Fonti} % (fold)\n")
        self.__write_doc_file.write("\label{ssub:requisiti_fonti}\n")
        self.__write_doc_file.write("\\begin{center}\n")
        self.__write_doc_file.write("\def\\arraystretch{1.5}\n")
        self.__write_doc_file.write("\\bgroup\n")
        self.__write_doc_file.write("\\begin{longtable}{| p{4cm} | p{4cm} |}\n")
        self.__write_doc_file.write("\hline\n")
        self.__write_doc_file.write("\\textbf{Requisito} & \\textbf{Fonti} \\\\\n")
        self.__write_doc_file.write("\hline\n")

        for val in self.__req_fonti_array:
            fonti_val = self.__req_fonti_dict[val]
            self.__write_doc_file.write(val + "  &  " + fonti_val + "\n")
            self.__write_doc_file.write("\hline\n")

        self.__write_doc_file.write("\end{longtable}\n")
        self.__write_doc_file.write("\egroup\n")
        self.__write_doc_file.write("\end{center}\n")
        self.__write_doc_file.write("% subsubsection requisiti_fonti (end)\n")

    def write_list_req(self):
        self.__write_list_req_str = "requisiti-componenti-base.tex"
        self.__write_list_req_file = open(self.__write_list_req_str, "w")
        self.__write_list_req_file.write("\subsection{Requisiti-Componenti} % (fold)\n")
        self.__write_list_req_file.write("\label{sub:componenti_requisiti}\n")
        self.__write_list_req_file.write("\\begin{center}\n")
        self.__write_list_req_file.write("\def\\arraystretch{1.5}\n")
        self.__write_list_req_file.write("\\bgroup\n")
        self.__write_list_req_file.write("\\begin{longtable}{| p{4cm} | p{8cm} |}\n")
        self.__write_list_req_file.write("\hline\n")
        self.__write_list_req_file.write("\\textbf{Requisito} & \\textbf{Componenti} \\\\\n")
        self.__write_list_req_file.write("\hline\n")

        for val in self.__req_fonti_array:
            val = val.strip()
            if val in self.__req_comp_dict:
                comp_for_req = self.__req_comp_dict[val]
                self.__write_list_req_file.write(val + " & ")
                length = len(comp_for_req)
                counter = 0
                for r in comp_for_req:
                    self.__write_list_req_file.write(r + " ")
                    counter += 1
                    if counter != length:
                        self.__write_list_req_file.write("\\newline ")
            else:
                self.__write_list_req_file.write(val + " & TO DO: Componente non tracciato! ")

            self.__write_list_req_file.write("\\\\\n")
            self.__write_list_req_file.write("\hline\n")

        self.__write_list_req_file.write("\end{longtable}\n")
        self.__write_list_req_file.write("\egroup\n")
        self.__write_list_req_file.write("\end{center}\n")
        self.__write_list_req_file.write("% subsection componenti_requisiti (end)\n")