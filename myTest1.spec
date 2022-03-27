describe("Testing #1", () => {
it ('Авторизация', () => {
	cy.visit('https://finance.dev.fabrique.studio/accounts/login/');
	cy.get('input[type="email"]').type('admin@admin.ad');
	cy.get('input[type="password"]').type('admin');
	cy.get('button[type="submit"]').click();
 });

it ('Результат', () => {
		cy.should('have.text','Добавить платёж');
	});
});