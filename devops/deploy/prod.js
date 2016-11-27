module.exports = function (shipit) {
  shipit.blTask('initVirtualenv', function() {
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
    var tasks
    if(shipit.config.hasDatabase){
      tasks = ['installVendors', 'upgradeDatabase', 'restartServer']
    } else {
      tasks = ['installVendors', 'restartServer']
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
