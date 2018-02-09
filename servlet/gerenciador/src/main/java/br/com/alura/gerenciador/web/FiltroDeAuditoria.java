package br.com.alura.gerenciador.web;

import java.io.IOException;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebFilter(urlPatterns = "/*")
public class FiltroDeAuditoria implements Filter {

	@Override
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
			throws IOException, ServletException {
		HttpServletRequest req = (HttpServletRequest) request;
		HttpServletResponse resp = (HttpServletResponse) response;
		
		Cookie cookie = new Cookies(req.getCookies()).buscaUsuarioLogado();
		String usuario = "<deslogado>";
		
	    if (cookie != null) {
	        usuario = cookie.getValue();
	        cookie.setMaxAge(10 * 60);
	        resp.addCookie(cookie);
	    }

		System.out.println("Usuário " + cookie.getValue() + " acessando a URI: " + req.getRequestURI());

		// Para seguir com a requisição após realizar o Filter
		chain.doFilter(request, response);
	}

}