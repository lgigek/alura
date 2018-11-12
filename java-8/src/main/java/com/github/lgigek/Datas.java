package com.github.lgigek;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.Month;
import java.time.Period;
import java.time.format.DateTimeFormatter;

public class Datas {

    public static void main(String[] args) {

        LocalDate hoje = LocalDate.now();

        LocalDate copa = LocalDate.of(2022, Month.OCTOBER, 14);
        Period periodo = Period.between(hoje, copa);
        LocalDateTime agora = LocalDateTime.now();

        DateTimeFormatter formatador = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        DateTimeFormatter formatadorComHoras = DateTimeFormatter.ofPattern("dd/MM/yyyy hh:mm");

        System.out.println("Data da copa: " + copa.format(formatador));
        System.out.println("Faltam " + periodo.getYears() + " anos para a copa");
        System.out.println(copa.format(formatador));
        System.out.println("Data e hora: " + agora.format(formatadorComHoras));

    }
}
