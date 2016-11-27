module.exports = function (shipit) {
    require('shipit-deploy')(shipit);
    require('shipit-submodule')(shipit);

    shipit.initConfig({
        default: {
            workspace: '/tmp/flask-api-starter-kit',
            repositoryUrl: 'git@github.com:antkahn/flask-api-starter-kit.git',
            serviceName: 'application',
            hasDatabase: true,
            ignores: ['.git', 'node_modules'],
            shallowClone: true,
            submodules: true,
            keepReleases: 3
        },
        prod: {
            servers: [{
                host: 'my-first-host.com',
                user: 'api'
            }, {
                host: 'my-first-host.com',
                user: 'api'
            }],
            branch: 'prod',
            deployTo: '/my/path/on/server/flask-api-starter-kit',
        }
    });

    shipit.on('published', function() {
        return shipit.start('install');
    });

    if(shipit.environment.indexOf(['prod'])) {
      require('./devops/deploy/prod.js')(shipit);
    } else {
      shipit.log("Unknwown environment: " + shipit.environment);
      exit(1);
    }
};
