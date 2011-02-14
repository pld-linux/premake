Summary:	Cross-platform build configuration tool
Summary(pl.UTF-8):	Międzyplatformowe narzędzie do budowy projektów
Name:		premake
Version:	4.3
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/premake/%{name}-%{version}-src.zip
# Source0-md5:	8cfafee76f9665c93b2e9ad15b015eb7
Patch0:		%{name}-manpage.patch
Patch1:		%{name}-system-lua.patch
Patch2:		%{name}-flags.patch
URL:		http://industriousone.com/premake/
BuildRequires:	lua51-devel
BuildRequires:	readline-devel
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Premake is a build configuration tool that can generate project files
for:
 - GNU make
 - Code::Blocks
 - CodeLite
 - MonoDevelop
 - SharpDevelop
 - Apple XCode
 - Microsoft Visual Studio

%description -l pl.UTF-8
Premake jest narzędziem do budowy projektów, które potrafi wygenerować
pliki projektów dla:
 - GNU make
 - Code::Blocks
 - CodeLite
 - MonoDevelop
 - SharpDevelop
 - Apple XCode
 - Microsoft Visual Studio

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p1

%build
cd build/gmake.unix
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags} `pkg-config lua51 --cflags`" \
	LDFLAGS="%{rpmldflags}" \
	verbose=true

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

cp -a bin/release/premake4 $RPM_BUILD_ROOT%{_bindir}
cp -a premake4.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt
%attr(755,root,root) %{_bindir}/premake4
%{_mandir}/man1/premake4.1*
