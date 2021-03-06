# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from plugins.models import Plugin, PluginVersion
from django.utils.translation import ugettext_lazy as _

# Plugins filtered views (need user parameter from request)
urlpatterns = patterns('plugins.views',
    # XML
    url(r'^plugins.xml$', 'xml_plugins', {}, name='xml_plugins'),
    url(r'^tags/(?P<tags>[^\/]+)/$', 'tags_plugins', {}, name='tags_plugins'),
    url(r'^my/$', 'my_plugins', {}, name='my_plugins'),
    url(r'^add/$', 'plugin_upload', {}, name='plugin_upload'),
    url(r'^user/(?P<username>\w+)/$', 'user_plugins', {}, name='user_plugins'),
    url(r'^user/(?P<username>\w+)/block/$', 'user_block', {}, name='user_block'),
    url(r'^user/(?P<username>\w+)/unblock/$', 'user_unblock', {}, name='user_unblock'),
    url(r'^user/(?P<username>\w+)/admin$', 'user_details', {}, name='user_details'),
    url(r'^user/(?P<username>\w+)/trust/$', 'user_trust', {}, name='user_trust'),
    url(r'^user/(?P<username>\w+)/untrust/$', 'user_untrust', {}, name='user_untrust'),

    url(r'^(?P<package_name>[^/]+)/manage/$', 'plugin_manage', {}, name='plugin_manage'),
    url(r'^(?P<package_name>[^/]+)/delete/$', 'plugin_delete', {}, name='plugin_delete'),
    url(r'^(?P<package_name>[^/]+)/update/$', 'plugin_update', {}, name='plugin_update'),
    url(r'^(?P<package_name>[^/]+)/$', 'plugin_detail', { 'queryset' : Plugin.objects.all() }, name='plugin_detail'),
    url(r'^(?P<package_name>[^/]+)/set_featured/$', 'plugin_set_featured', {}, name='plugin_set_featured'),
    url(r'^(?P<package_name>[^/]+)/unset_featured/$', 'plugin_unset_featured', {}, name='plugin_unset_featured'),

    url(r'^$', 'plugins_list', { 'queryset' : Plugin.approved_objects.all()}, name='approved_plugins'),
    url(r'^featured/$', 'plugins_list', {'queryset' : Plugin.featured_objects.all(), 'extra_context' : {'title' : _('Featured plugins')}}, name='featured_plugins'),
    url(r'^unapproved/$', 'plugins_list', {'queryset' : Plugin.unapproved_objects.all(), 'extra_context' : {'title' : _('Unapproved plugins')}}, name='unapproved_plugins'),
    url(r'^fresh/$', 'plugins_list', {'queryset' : Plugin.fresh_objects.all(), 'extra_context' : {'title' : _('Fresh plugins')}}, name='fresh_plugins'),
    url(r'^stable/$', 'plugins_list', {'queryset' : Plugin.stable_objects.all(), 'extra_context' : {'title' : _('Stable plugins')}}, name='stable_plugins'),
    url(r'^experimental/$', 'plugins_list', {'queryset' : Plugin.experimental_objects.all(), 'extra_context' : {'title' : _('Experimental plugins')}}, name='experimental_plugins'),
    url(r'^popular/$', 'plugins_list', {'queryset' : Plugin.popular_objects.all(), 'extra_context' : {'title' : _('Popular plugins')}}, name='popular_plugins'),
)


# User management
urlpatterns += patterns('plugins.views',
    url(r'^user/(?P<username>\w+)/manage/$', 'user_permissions_manage', {}, name='user_permissions_manage'),
)


# Version Management
urlpatterns += patterns('plugins.views',
    url(r'^version/(?P<package_name>[^/]+)/(?P<version>[^/]+)/manage/$', 'version_manage', {},  name='version_manage'),
    url(r'^version/(?P<package_name>[^/]+)/add/$', 'version_create', {}, name='version_create'),
    url(r'^version/(?P<package_name>[^/]+)/(?P<version>[^/]+)/$', 'version_detail', {}, name='version_detail'),
    url(r'^version/(?P<package_name>[^/]+)/(?P<version>[^/]+)/delete/$', 'version_delete', {}, name='version_delete'),
    url(r'^version/(?P<package_name>[^/]+)/(?P<version>[^/]+)/update/$', 'version_update', {}, name='version_update'),
    url(r'^version/(?P<package_name>[^/]+)/(?P<version>[^/]+)/download/$', 'version_download', {}, name='version_download'),
    url(r'^version/(?P<package_name>[^/]+)/(?P<version>[^/]+)/approve/$', 'version_approve', {}, name='version_approve'),
    url(r'^version/(?P<package_name>[^/]+)/(?P<version>[^/]+)/unapprove/$', 'version_unapprove', {}, name='version_unapprove'),
)

