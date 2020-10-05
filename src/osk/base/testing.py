# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import osk.base


class OskBaseLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=osk.base)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'osk.base:default')


OSK_BASE_FIXTURE = OskBaseLayer()


OSK_BASE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(OSK_BASE_FIXTURE,),
    name='OskBaseLayer:IntegrationTesting',
)


OSK_BASE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(OSK_BASE_FIXTURE,),
    name='OskBaseLayer:FunctionalTesting',
)


OSK_BASE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        OSK_BASE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='OskBaseLayer:AcceptanceTesting',
)
