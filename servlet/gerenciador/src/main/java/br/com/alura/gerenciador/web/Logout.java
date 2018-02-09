package br.com.alura.gerenciador.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(urlPatterns = "/logout")
public class Logout extends HttpServlet {

	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		Cookie cookieLogado = new Cookies(req.getCookies()).buscaUsuarioLogado();
		PrintWriter writer = resp.getWriter();

		if(cookieLogado == null) {
			writer.println("<html><body><h1>Usuário já estava deslogado</h1></body></html>");
			return;
		}
		
		cookieLogado.setMaxAge(0);
		resp.addCookie(cookieLogado);
		writer.println("<html><body><h1>Usuário deslogado com sucesso</h1></body></html>");
	}

}
