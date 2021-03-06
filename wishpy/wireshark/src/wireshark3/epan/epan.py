import sys

from cffi import FFI
try:
    from cffi import PkgConfigError
except:
    pass

if sys.platform == 'win32':
    from ...glib.glib_win_h import glib_h_cdef
    from ...wsutil.nstime_win_h import wsutil_nstime_h_types_cdef
else:
    from ...glib.glib_h import glib_h_cdef
    from ...wsutil.nstime_h import wsutil_nstime_h_types_cdef

from ...glib.garray_h import garray_h_cdef
from ...glib.glist_h import glist_h_cdef
from ...glib.gstring_h import glib_gstring_h_types_cdef
from ...glib.ghash_h import glib_ghash_h_types_cdef

from ...wsutil.buffer_h import wsutil_buffer_h_cdef
from ...wsutil.inet_ipv4_h import wsutil_inet_ipv4_h_cdef
from ...wsutil.inet_ipv6_h import wsutil_inet_ipv6_h_cdef
from ...wsutil.inet_addr_h import wsutil_inet_addr_h_cdef
from ...wsutil.plugins_h import wsutil_plugins_h_cdef
from ...wsutil.colors_h import wsutil_colors_h_cdef
#from ...wsutil.ws_mempbrk_h import wsutil_ws_mempbrk_h_types_cdef
from ...wsutil.privileges_h import wsutil_privileges_h_funcs_cdef
from ...wishpy_types_h import wishpy_types_h_cdef


from ..wtap.wtap_h import (
        wtap_h_types_cdef,
        wtap_h_funcs_cdef)

from ..wtap.wtap_opttypes_h import (
        wtap_opttypes_h_types_cdef,
        wtap_opttypes_h_funcs_cdef)

from .epan_h import epan_h_cdef
from .register_h import epan_register_h_types_cdef
from .framedata_h import (
        framedata_h_types_cdef,
        framedata_h_funcs_cdef
        )
from .prefs_h import epan_prefs_h_cdef
from .params_h import epan_params_h_cdef
from .range_h import epan_range_h_types_cdef
from .tvbuff_h import epan_tvbuff_h_types_cdef
from .tvbuff_h import epan_tvbuff_h_funcs_cdef
from .guid_utils_h import epan_guid_utils_h_types_cdef
from .wmem_h import epan_wmem_h_types_cdef
from .wmem_h import epan_wmem_h_funcs_cdef
from .packet_h import epan_packet_h_funcs_cdef, epan_packet_h_types_cdef
from .address_h import epan_address_h_types_cdef
from .packet_info_h import epan_packet_info_h_cdef
from .epan_dissect_h import epan_epan_dissect_h_types_cdef
from .proto_h import epan_proto_h_types_cdef
from .ftypes_h import epan_ftypes_h_types_cdef
from .ftypes_h import epan_ftypes_h_funcs_cdef
from .dfilter_h import (
        epan_dfilter_h_types_cdef,
        epan_dfilter_h_funcs_cdef
        )

epan_ffi = FFI()

epan_ffi.cdef(glib_h_cdef)
epan_ffi.cdef(garray_h_cdef)
epan_ffi.cdef(glist_h_cdef)
epan_ffi.cdef(glib_gstring_h_types_cdef)
epan_ffi.cdef(glib_ghash_h_types_cdef)

epan_ffi.cdef(wsutil_nstime_h_types_cdef)
epan_ffi.cdef(wsutil_buffer_h_cdef)
epan_ffi.cdef(wsutil_inet_ipv4_h_cdef)
epan_ffi.cdef(wsutil_inet_ipv6_h_cdef)
epan_ffi.cdef(wsutil_inet_addr_h_cdef)
epan_ffi.cdef(wsutil_plugins_h_cdef)
epan_ffi.cdef(wsutil_colors_h_cdef)
epan_ffi.cdef(wsutil_privileges_h_funcs_cdef)

epan_ffi.cdef(wtap_opttypes_h_types_cdef)
epan_ffi.cdef(wtap_opttypes_h_funcs_cdef)
epan_ffi.cdef(wtap_h_types_cdef)
epan_ffi.cdef(wtap_h_funcs_cdef)

epan_ffi.cdef(framedata_h_types_cdef)
epan_ffi.cdef(framedata_h_funcs_cdef)
epan_ffi.cdef(epan_register_h_types_cdef)
epan_ffi.cdef(epan_params_h_cdef)
epan_ffi.cdef(epan_range_h_types_cdef)
epan_ffi.cdef(epan_prefs_h_cdef)

#epan_ffi.cdef(wsutil_ws_mempbrk_h_types_cdef)
epan_ffi.cdef(epan_guid_utils_h_types_cdef)
epan_ffi.cdef(epan_wmem_h_types_cdef)
epan_ffi.cdef(epan_wmem_h_funcs_cdef)
epan_ffi.cdef(epan_tvbuff_h_types_cdef)
epan_ffi.cdef(epan_tvbuff_h_funcs_cdef)
epan_ffi.cdef(epan_address_h_types_cdef)
epan_ffi.cdef(epan_packet_info_h_cdef)
epan_ffi.cdef(epan_ftypes_h_types_cdef)
epan_ffi.cdef(epan_ftypes_h_funcs_cdef)
epan_ffi.cdef(epan_dfilter_h_types_cdef)
epan_ffi.cdef(epan_dfilter_h_funcs_cdef)
epan_ffi.cdef(epan_proto_h_types_cdef)
epan_ffi.cdef(epan_epan_dissect_h_types_cdef)
epan_ffi.cdef(epan_h_cdef)
epan_ffi.cdef(epan_packet_h_types_cdef)
epan_ffi.cdef(epan_packet_h_funcs_cdef)

# Add our own definitions
epan_ffi.cdef(wishpy_types_h_cdef)
# Go ahead and get the Library handle


_sources = '''
            #define HAVE_PLUGINS 1
            #include <epan/address.h>
            #include <epan/proto.h>
            #include <epan/epan_dissect.h>
            #include <epan/epan.h>
            #include <epan/packet.h>
            #include <epan/prefs.h>
            #include <epan/dfilter/dfilter.h>
            #include <wsutil/privileges.h>

            struct packet_provider_data {
                const frame_data *ref;
                const frame_data *prev;
            };
'''

_pkg_name = 'wishpy.wireshark.lib.epan3_ext'

_pkgconfig_libs = ['wireshark']

_libraries = ['glib-2.0', 'wireshark', 'wsutil', 'wiretap']

if sys.platform == 'win32':
    # FIXME: Remove the hardcoding below. Change following paths to match
    # Those on your machine.
    _extra_compile_args = [
            "-IC:\\Program Files (x86)\\Wireshark\\include\\Wireshark",
            "-IC:\\wireshark-dev\\wireshark-win64-libs-3.2\\vcpkg-export-20190318-win64ws\\installed\\x64-windows\\include"
            ]
    _extra_link_args = [
            "/LIBPATH:C:\\wireshark-dev\\wireshark-win64-libs-3.2\\vcpkg-export-20190318-win64ws\\installed\\x64-windows\\lib",
            "/LIBPATH:C:\\Program Files (x86)\\Wireshark"
        ]
else:
    _extra_compile_args = [
        '-I/usr/local/include/wireshark',
        '-I/usr/include/wireshark',
        '-I/usr/include/glib-2.0',
        '-I/usr/lib/x86_64-linux-gnu/glib-2.0/include',
        ]

    _extra_link_args = [
            '-L/usr/local/lib',
        ]

try:
    epan_ffi.set_source_pkgconfig(_pkg_name, _pkgconfig_libs, _sources,
            extra_link_args=_extra_link_args)
except PkgConfigError:
    epan_ffi.set_source(_pkg_name, _sources,
            extra_compile_args=_extra_compile_args,
            libraries=_libraries,
            extra_link_args=_extra_link_args)
