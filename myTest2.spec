describe("Test #2", () => {
it ('Авторизация', () => {
	cy.visit('https://finance.dev.fabrique.studio/accounts/login/?User ID=fabrique&Password=fabrique');
	cy.get('button[type="submit"]').click();
 });
 
it ('Результат Поиск', () => {
		cy.get('input[placeholder="Поиск"]').type('тест');
		cy.get('input[placeholder="Поиск"]').type('{enter}');
		cy.get('.table table--is-responsive').should('have.text','тест');
	});
});