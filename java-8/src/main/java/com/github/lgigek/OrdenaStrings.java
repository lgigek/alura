package com.github.lgigek;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.function.Consumer;

public class OrdenaStrings {

    public static void main(String[] args) {

        List<String> palavras = new ArrayList<String>();
        palavras.add("alura onlinte");
        palavras.add("editora casa do código");
        palavras.add("caelum");

        palavras.sort(Comparator.comparing(String::length));
        System.out.println(palavras);

        palavras.forEach(System.out::println);
    }
}