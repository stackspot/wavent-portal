var Ziggy = {
	url: 'http://localhost:8000',
	port: '8000',
	defaults: {},
	routes: {
		'users.index': { uri: 'admin/equipa', methods: ['GET'], bindings: {} },
		'users.create': {
			uri: 'admin/equipa/novo',
			methods: ['GET'],
			bindings: {},
		},
		'users.store': { uri: 'admin/equipa', methods: ['POST'], bindings: {} },
		'users.show': {
			uri: 'admin/equipa/{user}',
			methods: ['GET'],
			bindings: {},
		},
		'users.update': {
			uri: 'admin/equipa/{user}',
			methods: ['PUT'],
			bindings: {},
		},
		'users.destroy': {
			uri: 'admin/equipa/{user}',
			methods: ['DELETE'],
			bindings: {},
		},
		'client.index': { uri: 'admin/cliente', methods: ['GET'], bindings: {} },
		'client.create': {
			uri: 'admin/cliente/novo',
			methods: ['GET'],
			bindings: {},
		},
		'client.store': { uri: 'admin/cliente', methods: ['POST'], bindings: {} },
		'client.show': {
			uri: 'admin/cliente/{service}',
			methods: ['GET'],
			bindings: {},
		},
		'client.update': {
			uri: 'admin/cliente/{service}',
			methods: ['POST'],
			bindings: {},
		},
		'client.delete': {
			uri: 'admin/cliente/{service}/destroy',
			methods: ['DELETE'],
			bindings: {},
		},
		'account.index': { uri: 'admin/account', methods: ['GET'], bindings: {} },
		'account.store': {
			uri: 'admin/account/store',
			methods: ['POST'],
			bindings: {},
		},
		'account.profile': {
			uri: 'admin/account/{account}',
			methods: ['GET'],
			bindings: {},
		},
		'account.update': {
			uri: 'admin/account/{account}',
			methods: ['PUT'],
			bindings: {},
		},
		'account.destroy': {
			uri: 'admin/account/{account}',
			methods: ['DELETE'],
			bindings: {},
		},
		'account.settings': {
			uri: 'admin/account/settings',
			methods: ['GET'],
			bindings: {},
		},
		'organization.index': {
			uri: 'admin/empresa',
			methods: ['GET'],
			bindings: {},
		},
		'organization.store': {
			uri: 'admin/empresa',
			methods: ['POST'],
			bindings: {},
		},
		'organization.profile': {
			uri: 'admin/empresa/{organization}',
			methods: ['GET'],
			bindings: {},
		},
		'organization.update': {
			uri: 'admin/empresa/{organization}',
			methods: ['PUT'],
			bindings: {},
		},
		'organization.destroy': {
			uri: 'admin/empresa/{organization}',
			methods: ['DELETE'],
			bindings: {},
		},
		'organization.settings': {
			uri: 'admin/empresa/settings',
			methods: ['GET'],
			bindings: {},
		},
		'schedule.index': { uri: 'admin/schedule', methods: ['GET'], bindings: {} },
		'schedule.store': {
			uri: 'admin/schedule',
			methods: ['POST'],
			bindings: {},
		},
		'schedule.edit': {
			uri: 'admin/schedule/{schedule}/edit',
			methods: ['GET'],
			bindings: {},
		},
		'schedule.update': {
			uri: 'admin/schedule/{schedule}',
			methods: ['PUT'],
			bindings: {},
		},
		'appointment.index': {
			uri: 'admin/calendario',
			methods: ['GET'],
			bindings: {},
		},
		'appointment.store': {
			uri: 'admin/calendario/create',
			methods: ['POST'],
			bindings: {},
		},
		'appointment.edit': {
			uri: 'admin/calendario/{appointment}/edit',
			methods: ['GET'],
			bindings: {},
		},
		'appointment.update': {
			uri: 'admin/calendario/{appointment}',
			methods: ['PUT'],
			bindings: {},
		},
		'appointment.delete': {
			uri: 'admin/calendario/{appointment}',
			methods: ['DELETE'],
			bindings: {},
		},
		'appointment.settings': {
			uri: 'admin/calendario/settings',
			methods: ['GET'],
			bindings: {},
		},
		'service.index': { uri: 'admin/servicos', methods: ['GET'], bindings: {} },
		'service.create': {
			uri: 'admin/servicos/novo',
			methods: ['GET'],
			bindings: {},
		},
		'service.store': { uri: 'admin/servicos', methods: ['POST'], bindings: {} },
		'service.edit': {
			uri: 'admin/servicos/{service}/editar',
			methods: ['GET'],
			bindings: {},
		},
		'service.update': {
			uri: 'admin/servicos/{service}',
			methods: ['POST'],
			bindings: {},
		},
		'service.delete': {
			uri: 'admin/servicos/{service}',
			methods: ['DELETE'],
			bindings: {},
		},
		settings: { uri: 'admin/definicao', methods: ['GET'], bindings: {} },
		login: { uri: 'login', methods: ['GET'], bindings: {} },
		logout: { uri: 'logout', methods: ['GET'], bindings: {} },
		'auth.home': { uri: 'home', methods: ['GET'], bindings: {} },
		register: { uri: 'register', methods: ['GET'], bindings: {} },
		'register.store': { uri: 'register', methods: ['POST'], bindings: {} },
		password_reset: { uri: 'password_reset', methods: ['GET'], bindings: {} },
		'password_reset.store': {
			uri: 'password_reset',
			methods: ['POST'],
			bindings: {},
		},
		change_password: {
			uri: 'change_password/{token}',
			methods: ['GET'],
			bindings: {},
		},
		'change_password.store': {
			uri: 'change_password/{token}',
			methods: ['POST'],
			bindings: {},
		},
		'login.store': { uri: 'login', methods: ['POST'], bindings: {} },
	},
}

export { Ziggy }
