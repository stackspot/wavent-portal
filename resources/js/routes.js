var Ziggy = {
	url: 'http://localhost:8000',
	port: '8000',
	defaults: {},
	routes: {
		dashboard: { uri: 'admin', methods: ['GET'], bindings: {} },
		'users.index': {
			uri: 'admin/utilizadores',
			methods: ['GET'],
			bindings: {},
		},
		'users.create': {
			uri: 'admin/utilizadores/novo',
			methods: ['GET'],
			bindings: {},
		},
		'users.store': {
			uri: 'admin/utilizadores',
			methods: ['POST'],
			bindings: {},
		},
		'users.show': {
			uri: 'admin/utilizadores/{user}',
			methods: ['GET'],
			bindings: {},
		},
		'users.update': {
			uri: 'admin/utilizadores/{user}',
			methods: ['PUT'],
			bindings: {},
		},
		'users.destroy': {
			uri: 'admin/utilizadores/{user}',
			methods: ['DELETE'],
			bindings: {},
		},
		'staff.index': { uri: 'admin/equipa', methods: ['GET'], bindings: {} },
		'staff.create': {
			uri: 'admin/equipa/novo',
			methods: ['GET'],
			bindings: {},
		},
		'staff.store': { uri: 'admin/equipa', methods: ['POST'], bindings: {} },
		'staff.edit': {
			uri: 'admin/equipa/{staff}/editar',
			methods: ['GET'],
			bindings: {},
		},
		'staff.show': {
			uri: 'admin/equipa/{staff}',
			methods: ['GET'],
			bindings: {},
		},
		'staff.update': {
			uri: 'admin/equipa/{staff}',
			methods: ['PUT'],
			bindings: {},
		},
		'staff.destroy': {
			uri: 'admin/equipa/{staff}',
			methods: ['DELETE'],
			bindings: {},
		},
		'client.index': { uri: 'admin/cliente', methods: ['GET'], bindings: {} },
		'client.create': {
			uri: 'admin/cliente/novo',
			methods: ['GET'],
			bindings: {},
		},
		'client.edit': {
			uri: 'admin/cliente/{client}/editar',
			methods: ['GET'],
			bindings: {},
		},
		'client.store': { uri: 'admin/cliente', methods: ['POST'], bindings: {} },
		'client.show': {
			uri: 'admin/cliente/{client}',
			methods: ['GET'],
			bindings: {},
		},
		'client.update': {
			uri: 'admin/cliente/{client}',
			methods: ['POST'],
			bindings: {},
		},
		'client.delete': {
			uri: 'admin/cliente/{client}/destroy',
			methods: ['DELETE'],
			bindings: {},
		},
		'account.index': { uri: 'admin/conta', methods: ['GET'], bindings: {} },
		'account.store': {
			uri: 'admin/conta/store',
			methods: ['POST'],
			bindings: {},
		},
		'account.profile': {
			uri: 'admin/conta/{account}',
			methods: ['GET'],
			bindings: {},
		},
		'account.update': {
			uri: 'admin/conta/{account}',
			methods: ['PUT'],
			bindings: {},
		},
		'account.destroy': {
			uri: 'admin/conta/{account}',
			methods: ['DELETE'],
			bindings: {},
		},
		'account.settings': {
			uri: 'admin/conta/settings',
			methods: ['GET'],
			bindings: {},
		},
		'provider.index': { uri: 'admin/empresa', methods: ['GET'], bindings: {} },
		'provider.store': { uri: 'admin/empresa', methods: ['POST'], bindings: {} },
		'provider.profile': {
			uri: 'admin/empresa/{provider}',
			methods: ['GET'],
			bindings: {},
		},
		'provider.update': {
			uri: 'admin/empresa/{provider}',
			methods: ['PUT'],
			bindings: {},
		},
		'provider.destroy': {
			uri: 'admin/empresa/{provider}',
			methods: ['DELETE'],
			bindings: {},
		},
		'provider.settings': {
			uri: 'admin/empresa/settings',
			methods: ['GET'],
			bindings: {},
		},
		'schedule.index': { uri: 'admin/horario', methods: ['GET'], bindings: {} },
		'schedule.store': { uri: 'admin/horario', methods: ['POST'], bindings: {} },
		'schedule.edit': {
			uri: 'admin/horario/{schedule}/edit',
			methods: ['GET'],
			bindings: {},
		},
		'schedule.update': {
			uri: 'admin/horario/update',
			methods: ['POST'],
			bindings: {},
		},
		'appointment.index': {
			uri: 'admin/calendario',
			methods: ['GET'],
			bindings: {},
		},
		'appointment.api': {
			uri: 'admin/calendario/marcacoes',
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
