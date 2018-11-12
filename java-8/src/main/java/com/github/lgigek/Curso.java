package com.github.lgigek;

import java.util.*;
import java.util.stream.Collectors;

public class Curso {

    private String nome;
    private int alunos;

    public Curso(String nome, int alunos) {

        this.nome = nome;
        this.alunos = alunos;
    }

    public String getNome() {

        return nome;
    }

    public int getAlunos() {

        return alunos;
    }
}

class ExemploCursos {

    public static void main(String[] args) {

        List<Curso> cursos = new ArrayList<Curso>();
        cursos.add(new Curso("Python", 45));
        cursos.add(new Curso("JavaScript", 150));
        cursos.add(new Curso("Java 8", 113));
        cursos.add(new Curso("C", 55));

        cursos.sort(Comparator.comparing(Curso::getAlunos));

        cursos.stream()
                .filter(c -> c.getAlunos() >= 100)
                .mapToInt(Curso::getAlunos)
                .average()
                .ifPresent(m -> System.out.println("Média de alunos: " + m));

        cursos.stream()
                .filter(c -> c.getAlunos() >= 100)
                .findAny()
                .ifPresent(c -> System.out.println("Curso com mais de 100 alunos: " + c.getNome()));

        cursos.stream()
                .filter(c -> c.getAlunos() >= 100)
                .collect(Collectors.toMap(
                        c -> c.getNome(),
                        c -> c.getAlunos()))
                .forEach((nome, alunos) -> System.out.println(nome + " tem " + alunos));

    }

}