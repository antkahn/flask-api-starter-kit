module.exports = function (shipit) {
  var supervisorService = shipit.config.fullServiceName

  shipit.blTask('initVirtualenv', function() {
    oldVenv = shipit.currentPath + "/venv"
    return shipit.remote(
      "cd " + shipit.releasePath +
      " && virtualenv venv -p /usr/bin/python3" +
      " && source venv/bin/activate" +
      " && pip install --upgrade pip"
    );
  });

  shipit.blTask('installVendors', function() {
    return shipit.remote(
      "cd " + shipit.currentPath +
      " && source venv/bin/activate" +
      " && pip install --find-links=~/wheels -r requirements.txt --upgrade"
    );
  });

  shipit.blTask('upgradeDatabase', function() {
    return shipit.remote(
      "cd " + shipit.currentPath +
      " && source venv/bin/activate" +
      " && set -a && source " + shipit.config.deployTo + "/password.conf" +
      " && export PYTHONPATH=src" +
      " && cd " + shipit.currentPath +
      " && python3 src/manage.py db upgrade"
    );
  });

  shipit.blTask('install', function() {
    if(shipit.config.hasDatabase){
      var tasks = ['installVendors', 'upgradeDatabase', 'restartServer']
    } else {
      var tasks = ['installVendors', 'restartServer']
    }
    shipit.start(tasks, function(err) {
      if(!err){
        shipit.log('Install done!');
      }
    })
  });

  shipit.on('updated', function() {
      return shipit.start('initVirtualenv');
  });
};
