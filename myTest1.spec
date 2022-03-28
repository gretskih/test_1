describe("Test #1", () => {
it ('Авторизация', () => {
	cy.visit('https://finance.dev.fabrique.studio/accounts/login/?User ID=fabrique&Password=fabrique');
	cy.get('button[type="submit"]').click();
 });

it ('Результат', () => {
		cy.should('have.text','Добавить платёж');
	});
});