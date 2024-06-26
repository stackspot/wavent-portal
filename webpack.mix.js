/* Mix provides a clean, fluent API for defining some Webpack build steps for your Masonite
applications. By default, we are compiling the CSS file for the application as well as
bundling up all the JS files. */
const mix = require('laravel-mix')
const path = require('path')
const WindiCSSWebpackPlugin = require('windicss-webpack-plugin')

mix
	.js('resources/js/app.js', 'storage/compiled/js')
	.vue()
	.sourceMaps()
	.postCss('resources/css/app.css', 'storage/compiled/css', [
		//
	])

// add an alias to js code
mix.alias({
	'@': path.resolve('resources/js/'),
})

mix.webpackConfig({
	plugins: [new WindiCSSWebpackPlugin()],
	module: {
		rules: [
			/* {
				test: /\.mjs$/,
				resolve: { fullySpecified: false },
				include: /node_modules/,
				type: 'javascript/auto',
			}, */
		],
	},
})

// add version hash in production
if (mix.inProduction()) {
	mix.version()
}
// Disable compilation success notification
mix.disableSuccessNotifications()
