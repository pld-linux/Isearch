Summary:	Isearch text search engine
Summary(pl.UTF-8):   Isearch - silnik przeszukujący tekst
Name:		Isearch
Version:	1.47b
Release:	2
License:	distributable
Group:		Applications/Text
#Source0Download: http://www.etymon.com/tr.html
Source0:	http://www.etymon.com/software/Isearch/%{name}-%{version}.tar.gz
# Source0-md5:	70dbe58eb5d0271cf0daf60a65bfc234
URL:		http://www.etymon.com/tr.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Isearch is software for indexing and searching text documents. It
supports full text and field based search, relevance ranked results,
Boolean queries, and heterogeneous databases. Isearch can parse many
kinds of documents "out of the box," including HTML, mail folders,
list digests, SGML-style tagged data, and USMARC. It can be extended
to support other formats by creating descendant classes in C++ that
define the document structure. It is pretty easy to customize in this
way, provided that you know some C++ (and you will need to ftp the
source code). A CGI interface is also included for web based
searching.

%description -l pl.UTF-8
Isearch jest oprogramowaniem do indeksowania i przeszukiwania
dokumentów tekstowych. Obsługuje przeszukiwanie całego tekstu, na
podstawie pól i inne, a także bazy heterogeniczne. Isearch może
przeszukiwać wiele rodzajów dokumentów, w tym HTML, foldery pocztowe,
przeglądy list, tekst z tagami SGML oraz USMARC. Może być rozszerzony
aby obsługiwał inne formaty przez tworzenie klas w C++ definiujących
strukturę dokumentu. Jest łatwy do przystosowania pod warunkiem
znajomości C++ (potrzebny jest do tego kod źródłowy). Załączony jest
także interfejs CGI.

%prep
%setup -q -n %{name}

%build
%configure2_13
%{__make} \
	CFLAGS="-DUNIX -fwritable-strings -fno-rtti -fno-exceptions %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/home/httpd/{cgi-bin,databases},%{_bindir}}

./Isearch-cgi/Configure /home/httpd/databases %{_bindir}

%{__make} install \
	INSTALL=$RPM_BUILD_ROOT%{_bindir} \
	CGI_INSTALL=$RPM_BUILD_ROOT/home/httpd/cgi-bin

install Isearch-cgi/isrch_srch $RPM_BUILD_ROOT%{_bindir}
install Isearch-cgi/isrch_fetch $RPM_BUILD_ROOT%{_bindir}
install Isearch-cgi/isrch_html $RPM_BUILD_ROOT%{_bindir}
install Isearch-cgi/search_form $RPM_BUILD_ROOT%{_bindir}
install isearch $RPM_BUILD_ROOT/home/httpd/cgi-bin
install ifetch $RPM_BUILD_ROOT/home/httpd/cgi-bin
install ihtml $RPM_BUILD_ROOT/home/httpd/cgi-bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES COPYRIGHT README
%attr(755,root,root) %{_bindir}/Iindex
%attr(755,root,root) %{_bindir}/Isearch
%attr(755,root,root) %{_bindir}/Iutil
%attr(755,root,root) %{_bindir}/isrch_srch
%attr(755,root,root) %{_bindir}/isrch_fetch
%attr(755,root,root) %{_bindir}/isrch_html
%attr(755,root,root) %{_bindir}/search_form
%dir /home/httpd/databases
/home/httpd/cgi-bin/isearch
/home/httpd/cgi-bin/ifetch
/home/httpd/cgi-bin/ihtml
