'use strict'

describe 'Controller: ReportCtrl', (not-it) ->

  # load the controller's module
  beforeEach module 'roadpinFrontendApp'

  ReportCtrl = {}
  scope = {}

  # Initialize the controller and a mock scope
  beforeEach inject ($controller, $rootScope) ->
    scope := $rootScope.$new!
    ReportCtrl := $controller 'ReportCtrl', do
      $scope: scope
