#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	libsoup2	# libsoup 2.x based libraries (snapd-glib, snapd-qt5)
%bcond_without	libsoup3	# libsoup 3.x based libraries (snapd-glib-2, snapd-qt5-2)
%bcond_without	qt5		# Qt5/Qml bindings
%bcond_with	qt6		# Qt6/Qml bindings
%bcond_without	static_libs	# static libraries
#
%if %{with qt6}
# mutually exclusive, library names are the same
%undefine	with_qt5
%endif
Summary:	Library to allow GLib based applications access to snapd
Summary(pl.UTF-8):	Biblioteka umożliwiająca dostęp do snapd aplikacjom opartym na GLibie 
Name:		snapd-glib
Version:	1.66
Release:	1
License:	LGPL v2 or LGPL v3
Group:		Libraries
#Source0Download: https://github.com/canonical/snapd-glib/releases
Source0:	https://github.com/canonical/snapd-glib/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	c2f1c479004f7a8cc0c3a1503d79a147
URL:		https://github.com/canonical/snapd-glib
BuildRequires:	glib2-devel >= 1:2.46
BuildRequires:	gobject-introspection-devel
BuildRequires:	json-glib-devel >= 1.1.2
%{?with_libsoup2:BuildRequires:	libsoup-devel >= 2.32}
%{?with_libsoup3:BuildRequires:	libsoup3-devel >= 3.0}
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	meson >= 0.58.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	xz
%if %{with qt5}
BuildRequires:	Qt5Core-devel >= 5.9.5
BuildRequires:	Qt5Network-devel >= 5.9.5
BuildRequires:	Qt5Qml-devel >= 5.9.5
BuildRequires:	qt5-build >= 5.9.5
%endif
%if %{with qt6}
BuildRequires:	Qt6Core-devel >= 6.2.4
BuildRequires:	Qt6Network-devel >= 6.2.4
BuildRequires:	Qt6Qml-devel >= 6.2.4
BuildRequires:	qt6-build >= 6.2.4
%endif
Requires:	glib2 >= 1:2.46
Requires:	json-glib >= 1.1.2
Requires:	libsoup >= 2.32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
snapd-glib is a library to allow GLib based applications access to
snapd, the daemon that controls Snaps.

%description -l pl.UTF-8
snapd-glib to biblioteka pozwalająca na dostęp aplikacji opartych na
GLibie do snapd - demona kontrolującego Snapy.

%package devel
Summary:	Header files for snapd-glib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki snapd-glib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.46
Requires:	json-glib-devel >= 1.1.2
Requires:	libsoup-devel >= 2.32

%description devel
Header files for snapd-glib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki snapd-glib.

%package static
Summary:	Static snapd-glib library
Summary(pl.UTF-8):	Statyczna biblioteka snapd-glib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static snapd-glib library.

%description static -l pl.UTF-8
Statyczna biblioteka snapd-glib.

%package -n vala-snapd-glib
Summary:	Vala API for snapd-glib library
Summary(pl.UTF-8):	API języka Vala do biblioteki snapd-glib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala
BuildArch:	noarch

%description -n vala-snapd-glib
Vala API for snapd-glib library.

%description -n vala-snapd-glib -l pl.UTF-8
API języka Vala do biblioteki snapd-glib.

%package 2
Summary:	Library to allow GLib based applications access to snapd using libsoup3
Summary(pl.UTF-8):	Biblioteka umożliwiająca dostęp do snapd przy użyciu libsoup3 aplikacjom opartym na GLibie
Group:		Libraries
Requires:	glib2 >= 1:2.46
Requires:	json-glib >= 1.1.2
Requires:	libsoup3 >= 3.0

%description 2
snapd-glib-2 is a library to allow GLib based applications access to
snapd, the daemon that controls Snaps.

%description 2 -l pl.UTF-8
snapd-glib-2 to biblioteka pozwalająca na dostęp aplikacji opartych na
GLibie do snapd - demona kontrolującego Snapy.

%package 2-devel
Summary:	Header files for snapd-glib-2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki snapd-glib-2
Group:		Development/Libraries
Requires:	%{name}-2 = %{version}-%{release}
Requires:	glib2-devel >= 1:2.46
Requires:	json-glib-devel >= 1.1.2
Requires:	libsoup3-devel >= 3.0

%description 2-devel
Header files for snapd-glib-2 library.

%description 2-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki snapd-glib-2.

%package 2-static
Summary:	Static snapd-glib-2 library
Summary(pl.UTF-8):	Statyczna biblioteka snapd-glib-2
Group:		Development/Libraries
Requires:	%{name}-2-devel = %{version}-%{release}

%description 2-static
Static snapd-glib-2 library.

%description 2-static -l pl.UTF-8
Statyczna biblioteka snapd-glib-2.

%package -n vala-snapd-glib-2
Summary:	Vala API for snapd-glib-2 library
Summary(pl.UTF-8):	API języka Vala do biblioteki snapd-glib-2
Group:		Development/Libraries
Requires:	%{name}-2-devel = %{version}-%{release}
Requires:	vala
BuildArch:	noarch

%description -n vala-snapd-glib-2
Vala API for snapd-glib-2 library.

%description -n vala-snapd-glib-2 -l pl.UTF-8
API języka Vala do biblioteki snapd-glib-2.

%package apidocs
Summary:	API documentation for snapd-glib library
Summary(pl.UTF-8):	Dokumentacja API biblioteki snapd-glib
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for snapd-glib library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki snapd-glib.

%package -n snapd-qt5
Summary:	Library to allow Qt 5 based applications access to snapd
Summary(pl.UTF-8):	Biblioteka umożliwiająca dostęp do snapd aplikacjom opartym na Qt 5
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core >= 5.9.5
Requires:	Qt5Network >= 5.9.5

%description -n snapd-qt5
snapd-qt is a library to allow Qt based applications access to snapd,
the daemon that controls Snaps.

%description -n snapd-qt5 -l pl.UTF-8
snapd-qt to biblioteka pozwalająca na dostęp aplikacji opartych na Qt
do snapd - demona kontrolującego Snapy.

%package -n snapd-qt5-devel
Summary:	Header files for snapd-qt library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki snapd-qt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	Qt5Core-devel >= 5.9.5
Requires:	Qt5Network-devel >= 5.9.5
Requires:	snapd-qt5-devel = %{version}-%{release}

%description -n snapd-qt5-devel
Header files for snapd-qt library.

%description -n snapd-qt5-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki snapd-qt.

%package -n snapd-qt5-static
Summary:	Static snapd-qt library
Summary(pl.UTF-8):	Statyczna biblioteka snapd-qt
Group:		Development/Libraries
Requires:	snapd-qt5-devel = %{version}-%{release}

%description -n snapd-qt5-static
Static snapd-qt library.

%description -n snapd-qt5-static -l pl.UTF-8
Statyczna biblioteka snapd-qt.

%package -n snapd-qt5-2
Summary:	Library to allow Qt 5 based applications access to snapd using libsoup3
Summary(pl.UTF-8):	Biblioteka umożliwiająca dostęp do snapd aplikacjom opartym na Qt 5 przy użyciu libsoup3
Group:		Libraries
Requires:	%{name}-2 = %{version}-%{release}
Requires:	Qt5Core >= 5.9.5
Requires:	Qt5Network >= 5.9.5

%description -n snapd-qt5-2
snapd-qt-2 is a library to allow Qt based applications access to
snapd, the daemon that controls Snaps.

%description -n snapd-qt5-2 -l pl.UTF-8
snapd-qt-2 to biblioteka pozwalająca na dostęp aplikacji opartych na
Qt do snapd - demona kontrolującego Snapy.

%package -n snapd-qt5-2-devel
Summary:	Header files for snapd-qt-2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki snapd-qt-2
Group:		Development/Libraries
Requires:	%{name}-2-devel = %{version}-%{release}
Requires:	Qt5Core-devel >= 5.9.5
Requires:	Qt5Network-devel >= 5.9.5
Requires:	snapd-qt5-2-devel = %{version}-%{release}

%description -n snapd-qt5-2-devel
Header files for snapd-qt-2 library.

%description -n snapd-qt5-2-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki snapd-qt-2.

%package -n snapd-qt5-2-static
Summary:	Static snapd-qt-2 library
Summary(pl.UTF-8):	Statyczna biblioteka snapd-qt-2
Group:		Development/Libraries
Requires:	snapd-qt5-2-devel = %{version}-%{release}

%description -n snapd-qt5-2-static
Static snapd-qt-2 library.

%description -n snapd-qt5-2-static -l pl.UTF-8
Statyczna biblioteka snapd-qt-2.

%package -n snapd-qt6
Summary:	Library to allow Qt 6 based applications access to snapd
Summary(pl.UTF-8):	Biblioteka umożliwiająca dostęp do snapd aplikacjom opartym na Qt 6
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt6Core >= 6.2.4
Requires:	Qt6Network >= 6.2.4

%description -n snapd-qt6
snapd-qt is a library to allow Qt based applications access to snapd,
the daemon that controls Snaps.

%description -n snapd-qt6 -l pl.UTF-8
snapd-qt to biblioteka pozwalająca na dostęp aplikacji opartych na Qt
do snapd - demona kontrolującego Snapy.

%package -n snapd-qt6-devel
Summary:	Header files for snapd-qt library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki snapd-qt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	Qt6Core-devel >= 6.2.4
Requires:	Qt6Network-devel >= 6.2.4
Requires:	snapd-qt6-devel = %{version}-%{release}

%description -n snapd-qt6-devel
Header files for snapd-qt library.

%description -n snapd-qt6-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki snapd-qt.

%package -n snapd-qt6-static
Summary:	Static snapd-qt library
Summary(pl.UTF-8):	Statyczna biblioteka snapd-qt
Group:		Development/Libraries
Requires:	snapd-qt6-devel = %{version}-%{release}

%description -n snapd-qt6-static
Static snapd-qt library.

%description -n snapd-qt6-static -l pl.UTF-8
Statyczna biblioteka snapd-qt.

%package -n snapd-qt6-2
Summary:	Library to allow Qt 6 based applications access to snapd using libsoup3
Summary(pl.UTF-8):	Biblioteka umożliwiająca dostęp do snapd aplikacjom opartym na Qt 6 przy użyciu libsoup3
Group:		Libraries
Requires:	%{name}-2 = %{version}-%{release}
Requires:	Qt6Core >= 6.2.4
Requires:	Qt6Network >= 6.2.4

%description -n snapd-qt6-2
snapd-qt-2 is a library to allow Qt based applications access to
snapd, the daemon that controls Snaps.

%description -n snapd-qt6-2 -l pl.UTF-8
snapd-qt-2 to biblioteka pozwalająca na dostęp aplikacji opartych na
Qt do snapd - demona kontrolującego Snapy.

%package -n snapd-qt6-2-devel
Summary:	Header files for snapd-qt-2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki snapd-qt-2
Group:		Development/Libraries
Requires:	%{name}-2-devel = %{version}-%{release}
Requires:	Qt6Core-devel >= 6.2.4
Requires:	Qt6Network-devel >= 6.2.4
Requires:	snapd-qt6-2-devel = %{version}-%{release}

%description -n snapd-qt6-2-devel
Header files for snapd-qt-2 library.

%description -n snapd-qt6-2-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki snapd-qt-2.

%package -n snapd-qt6-2-static
Summary:	Static snapd-qt-2 library
Summary(pl.UTF-8):	Statyczna biblioteka snapd-qt-2
Group:		Development/Libraries
Requires:	snapd-qt6-2-devel = %{version}-%{release}

%description -n snapd-qt6-2-static
Static snapd-qt-2 library.

%description -n snapd-qt6-2-static -l pl.UTF-8
Statyczna biblioteka snapd-qt-2.

%prep
%setup -q

%build
for soupkind in %{?with_libsoup2:soup2} %{?with_libsoup3:soup3} ; do
%meson build-${soupkind} \
	%{!?with_static_libs:--default-library=shared} \
	%{!?with_apidocs:-Ddocs=false} \
	%{?with_qt5:-Dqt5=true} \
	%{!?with_qt6:-Dqt6=false} \
	$([ "$soupkind" = "soup2" ] && echo -Dsoup2=true)

%ninja_build -C build-${soupkind}
done

%install
rm -rf $RPM_BUILD_ROOT

for soupkind in %{?with_libsoup2:soup2} %{?with_libsoup3:soup3} ; do
%ninja_install -C build-${soupkind}
done

%if (%{with qt5} || %{with qt6}) && %{with static_libs}
%if %{with libsoup2}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/qt5/qml/Snapd/libSnapd.a
%endif
%if %{with libsoup3}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/qt5/qml/Snapd2/libSnapd2.a
%endif
%endif

%{__rm} -r $RPM_BUILD_ROOT{%{_libexecdir},%{_datadir}}/installed-tests

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	2 -p /sbin/ldconfig
%postun	2 -p /sbin/ldconfig

%post	-n snapd-qt5 -p /sbin/ldconfig
%postun	-n snapd-qt5 -p /sbin/ldconfig

%post	-n snapd-qt5-2 -p /sbin/ldconfig
%postun	-n snapd-qt5-2 -p /sbin/ldconfig

%post	-n snapd-qt6 -p /sbin/ldconfig
%postun	-n snapd-qt6 -p /sbin/ldconfig

%post	-n snapd-qt6-2 -p /sbin/ldconfig
%postun	-n snapd-qt6-2 -p /sbin/ldconfig

%if %{with libsoup2}
%files
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_libdir}/libsnapd-glib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsnapd-glib.so.1
%{_libdir}/girepository-1.0/Snapd-1.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsnapd-glib.so
%{_includedir}/snapd-glib
%{_datadir}/gir-1.0/Snapd-1.gir
%{_pkgconfigdir}/snapd-glib.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libsnapd-glib.a
%endif

%files -n vala-snapd-glib
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/snapd-glib.deps
%{_datadir}/vala/vapi/snapd-glib.vapi
%endif

%if %{with libsoup3}
%files 2
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_libdir}/libsnapd-glib-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsnapd-glib-2.so.1
%{_libdir}/girepository-1.0/Snapd-2.typelib

%files 2-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsnapd-glib-2.so
%{_includedir}/snapd-glib-2
%{_datadir}/gir-1.0/Snapd-2.gir
%{_pkgconfigdir}/snapd-glib-2.pc

%if %{with static_libs}
%files 2-static
%defattr(644,root,root,755)
%{_libdir}/libsnapd-glib-2.a
%endif

%files -n vala-snapd-glib-2
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/snapd-glib-2.deps
%{_datadir}/vala/vapi/snapd-glib-2.vapi
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/snapd-glib
%endif

%if %{with qt5}
%if %{with libsoup2}
%files -n snapd-qt5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsnapd-qt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsnapd-qt.so.1
%dir %{_libdir}/qt5/qml/Snapd
%attr(755,root,root) %{_libdir}/qt5/qml/Snapd/libSnapd.so
%{_libdir}/qt5/qml/Snapd/qmldir

%files -n snapd-qt5-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsnapd-qt.so
%{_includedir}/snapd-qt
%{_pkgconfigdir}/snapd-qt.pc
%{_libdir}/cmake/Snapd

%if %{with static_libs}
%files -n snapd-qt5-static
%defattr(644,root,root,755)
%{_libdir}/libsnapd-qt.a
%endif
%endif

%if %{with libsoup3}
%files -n snapd-qt5-2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsnapd-qt-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsnapd-qt-2.so.1
%dir %{_libdir}/qt5/qml/Snapd2
%attr(755,root,root) %{_libdir}/qt5/qml/Snapd2/libSnapd2.so
%{_libdir}/qt5/qml/Snapd2/qmldir

%files -n snapd-qt5-2-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsnapd-qt-2.so
%{_includedir}/snapd-qt-2
%{_pkgconfigdir}/snapd-qt-2.pc
%{_libdir}/cmake/Snapd2

%if %{with static_libs}
%files -n snapd-qt5-2-static
%defattr(644,root,root,755)
%{_libdir}/libsnapd-qt-2.a
%endif
%endif
%endif

%if %{with qt6}
%if %{with libsoup2}
%files -n snapd-qt6
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsnapd-qt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsnapd-qt.so.1
%dir %{_libdir}/qt6/qml/Snapd
%attr(755,root,root) %{_libdir}/qt6/qml/Snapd/libSnapd.so
%{_libdir}/qt6/qml/Snapd/qmldir

%files -n snapd-qt6-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsnapd-qt.so
%{_includedir}/snapd-qt
%{_pkgconfigdir}/snapd-qt.pc
%{_libdir}/cmake/Snapd

%if %{with static_libs}
%files -n snapd-qt6-static
%defattr(644,root,root,755)
%{_libdir}/libsnapd-qt.a
%endif
%endif

%if %{with libsoup3}
%files -n snapd-qt6-2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsnapd-qt-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsnapd-qt-2.so.1
%dir %{_libdir}/qt6/qml/Snapd2
%attr(755,root,root) %{_libdir}/qt6/qml/Snapd2/libSnapd2.so
%{_libdir}/qt6/qml/Snapd2/qmldir

%files -n snapd-qt6-2-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsnapd-qt-2.so
%{_includedir}/snapd-qt-2
%{_pkgconfigdir}/snapd-qt-2.pc
%{_libdir}/cmake/Snapd2

%if %{with static_libs}
%files -n snapd-qt6-2-static
%defattr(644,root,root,755)
%{_libdir}/libsnapd-qt-2.a
%endif
%endif
%endif
