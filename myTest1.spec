describe("Test #1", () => {
it ('Авторизация 1', () => {
	cy.visit('https://finance.dev.fabrique.studio/accounts/login/?User ID=fabrique&Password=fabrique');
	cy.get('button[type="submit"]').click();
 });

 it ('Авторизация 2', () => {
 	cy.get('input[type="email"]').type('admin@admin.ad');
 	cy.get('input[type="password"]').type('admin');
	cy.get('button[type="submit"]').click();
 }); 


it ('Результат', () => {
		cy.should('have.text','Добавить платёж');
	});
}); 