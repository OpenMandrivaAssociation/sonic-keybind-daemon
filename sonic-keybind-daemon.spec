%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname SonicDEKeybindDaemon
%define devname %mklibname SonicDEKeybindDaemon -d
#define git 20240222
%define gitbranch Plasma/6.6
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name: sonic-keybind-daemon
Version: 6.6.5
Release: %{?git:0.%{git}.}1
URL:     https://github.com/Sonic-DE/sonic-keybind-daemon
# %if 0%{?git:1}
# Source0: https://invent.kde.org/plasma/kglobalacceld/-/archive/%{gitbranch}/kglobalacceld-%{gitbranchd}.tar.bz2#/kglobalacceld-%{git}.tar.bz2
# %else
Source0: %url/archive/%version/%name-%version.tar.gz
# %endif
Summary: Daemon providing Global Keyboard Shortcut (Accelerator) functionality
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)

# pending rename
#BuildRequires: cmake(KF6KIO)
BuildRequires: %{_lib}SonicFrameworksIO-devel

BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Service)

# pending rename
# BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: %{_lib}SonicFrameworksKeybind-devel

# pending rename
# BuildRequires: cmake(KF6WindowSystem)
BuildRequires: %{_lib}SonicFrameworksWindowSystem-devel

BuildRequires: pkgconfig(x11-xcb)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xkbcommon)
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
Requires: %{libname} = %{EVRD}

Conflicts:    kaccelglobald

%description
Daemon providing Global Keyboard Shortcut (Accelerator) functionality

%package -n %{libname}
Summary: Daemon providing Global Keyboard Shortcut (Accelerator) functionality
Group: System/Libraries
Requires: %{name} = %{EVRD}
Conflicts: %{_lib}KGlobalAccelD

%description -n %{libname}
Daemon providing Global Keyboard Shortcut (Accelerator) functionality

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Conflicts: %{_lib}KGlobalAccelD-devel

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Daemon providing Global Keyboard Shortcut (Accelerator) functionality

%files
%{_sysconfdir}/xdg/autostart/kglobalacceld.desktop
%{_datadir}/qlogging-categories6/kglobalacceld.categories
%{_prefix}/lib/systemd/user/plasma-kglobalaccel.service
%{_qtdir}/plugins/org.kde.kglobalacceld.platforms
%{_libdir}/libexec/kglobalacceld

%files -n %{devname}
%{_includedir}/KGlobalAccelD
%{_libdir}/cmake/KGlobalAccelD

%files -n %{libname}
%{_libdir}/libKGlobalAccelD.so*
