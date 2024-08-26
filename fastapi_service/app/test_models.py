from sqlalchemy import Column, String, Numeric, Integer, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Objeto(Base):
    __tablename__ = 'objetos'

    ojtid = Column(Integer, primary_key=True, index=True)
    ojtidentificador1 = Column(String, index=True)
    ojtdistrito = Column(String)
    ojtruta = Column(String)

class LoteLiquidacion(Base):
    __tablename__ = 'lote_liquidacion'

    LLNID = Column(Integer, primary_key=True)  # Id de Lote de Liquidaciones
    LLNFECHAGENERACION = Column(DateTime)  # Fecha Generacion
    LLNCANTIDADLIQUIDACIONES = Column(Float)  # Cantidad Liquidaciones
    TLQID = Column(Integer)  # ID# Tipo Liquidacion
    LLNCRITERIOAGRUPAMIENTO = Column(String(20))  # Criterio Agrupamiento
    PSNID = Column(Integer)  # Persona ID
    TIPOOJT = Column(Integer)  # Tipo Ojt
    OJTID = Column(Integer)  # ID del Objeto
    ITSID = Column(String(5))  # Tributo
    CCTID = Column(String(5))  # ID# Concepto
    SCCID = Column(String(5))  # Subconcepto
    LLNFECHAVTODESDE = Column(DateTime)  # Fecha Vto Desde
    LLNFECHAVTOHASTA = Column(DateTime)  # Fecha Vto Hasta
    LLNUSUARIOALTA = Column(String(40))  # Lln Usuario Alta
    EGLID = Column(String(7))  # Estado de Generacion de Lote
    LLNFECHAALTA = Column(DateTime)  # Lln Fecha Alta
    LLNUSUARIOMODIFICACION = Column(String(40))  # Lln Usuario Modificacion
    LLNFECHAMODIFICACION = Column(DateTime)  # Lln Fecha Modificacion
    LLNUSUARIOBAJA = Column(String(40))  # Lln Usuario Baja
    LLNFECHABAJA = Column(DateTime)  # Lln Fecha Baja
    LLNFECHAINICIO = Column(DateTime)  # Lln Fecha Inicio
    LLNFECHAFIN = Column(DateTime)  # Lln Fecha Fin
    LLNFECHANOTA = Column(DateTime)  # Lln Fecha Nota
    TLLID = Column(String(5))  # Campo adicional TLLID
    LLNMOTIVO = Column(String(255))  # Motivo
    LLNTEXTO = Column(String(4000))  # Texto
    LLNTITULOANEXO4 = Column(String(30))  # Título Anexo 4
    LLNTITULOANEXO3 = Column(String(30))  # Título Anexo 3
    LLNTITULOANEXO2 = Column(String(30))  # Título Anexo 2
    LLNTITULOANEXO1 = Column(String(30))  # Título Anexo 1
    LLNREFERENCIA = Column(String(150))  # Referencia
    LLNTITULO2 = Column(String(150))  # Título 2
    LLNTITULO1 = Column(String(150))  # Título 1
    LLNDUPLICADO = Column(String(1))  # Duplicado
    LLNCADUCOS = Column(String(1))  # Caducos
    LLNNOCADUCOS = Column(String(1))  # No Caducos
    LLNOBSERVACIONES = Column(String(400))  # Observaciones
    LLNNOTA = Column(String(255))  # Nota
    LLNGENERADO = Column(String(1))  # Generado
    LLNNIVELPOSTINTI = Column(String(1))  # Nivel Post Inti
    LLNFECHAPOSTINTI = Column(DateTime)  # Fecha Post Inti
    LLNEXCLUIRPAGOS = Column(String(1))  # Excluir Pagos
    LLNCUOTASMINIMO = Column(Integer)  # Cuotas Mínimo
    LLNMONTOMINIMO = Column(Float)  # Monto Mínimo
    LLNDISTRITO = Column(String(2))  # Distrito
    LLNRUTADESDE = Column(Integer)  # Ruta Desde
    LLNRUTAHASTA = Column(Integer)  # Ruta Hasta
    LLNFOLIODESDE = Column(Integer)  # Folio Desde
    LLNFOLIOHASTA = Column(Integer)  # Folio Hasta

class TitulosDeuda(Base):
    __tablename__ = 'titulos_deuda'

    TITID = Column(Integer, primary_key=True)  # Id Interno: TABLA TITULO_DEUDA
    LLNID = Column(Integer)  # Id Externo: TABLA LOTE_LIQUIDACION
    TITEXTERNO = Column(Numeric(18, 0))  # TITULO PROVISORIO DE DEUDA EXTERNO
    TBJID = Column(Integer)  # Id Externo: TABLA TIPO_BAJA_LIQUIDACION
    JZGID = Column(String(5))  # id Juzgado
    TITFECHAGENERACION = Column(Date)  # Fecha de Generacion del Titulo Deuda
    TITFECHAIMPRESION = Column(Date)  # Fecha de Impresion
    TITFECHANOTIFICACION = Column(Date)  # Fecha de Notificacion
    TITNROEXPEDIENTE = Column(String(40))  # Nro de Expediente
    TITSECRETARIA = Column(String(40))  # Secretaria 
    TITIMPORTE = Column(Numeric(17, 2))  # Importe
    TITOBSERVACIONES = Column(String(100))  # Observaciones
    TITFECHAINICIO = Column(Date)  # Vigencia desde del Titulo Deuda
    TITFECHAFIN = Column(Date)  # Vigencia Desde del Titulo Deuda
    TITUSUARIOALTA = Column(String(40))  # Auditoria Usuario Alta
    TITFECHAALTA = Column(Date)  # Auditoria Fecha Alta
    TITUSUARIOMODIFICACION = Column(String(40))  # Auditoria Usuario Modificacion
    TITFECHAMODIFICACION = Column(Date)  # Auditoria Fecha Modificacion
    TITUSUARIOBAJA = Column(String(40))  # Auditoria Usuario Baja
    TITFECHABAJA = Column(Date)  # Auditoria Fecha Baja
    LIPOJTID = Column(Integer)  # Nro Liquidacion Privisoria Del Objeto
    LIPPSNID = Column(Integer)  # Nro Liquidacion Privisoria De la Persona
    TITCASO = Column(String(30))  # Caso
    TITCODCARTA = Column(String(40))  # Codigo de Carta
    TITFECHACARTA = Column(Date)  # Fecha de Carta
    TITCALLEFISCAL = Column(String(240))  # Calle (Fiscal)
    TITALTURAFISCAL = Column(String(10))  # Nro (Fiscal)
    TITPISOFISCAL = Column(String(10))  # Piso (Fiscal)
    TITDEPTOFISCAL = Column(String(4))  # Departamento (Fiscal)
    TITBARRIOFISCAL = Column(String(100))  # Barrio (Fiscal)
    TITLOCALIDADFISCAL = Column(String(100))  # Localidad (Fiscal)
    TITPROVINCIAFISCAL = Column(String(100))  # Provincia (Fiscal)
    TITCODIGOPOSTAL = Column(String(40))  # Codigo Postal
    TITORIGENDOMICILIO = Column(String(40))  # Domicilio de Origen
    TITUNIVERSO = Column(Numeric(12, 0))  # REFSA: Nro de Universo del PDA 
    TITDEPARTAMENTOFISCAL = Column(String(100))  # Fiscalia
    TITCIRCUNSCRIPCIONJUDICIAL = Column(Integer)  # Circuncripcion Judicial
    TITDENOMINACIONINFRACTOR = Column(String(200))  # Nombre del Infractor
    TITCUITINFRACTOR = Column(String(200))  # CUIT del Infractor
    TITFECRESOLUCION = Column(Date)  # Fecha De la Resolucion
    TITDOMINIO = Column(String(40))  # Dominio
    TITTIPOTRAMITEBAJA = Column(String(15))  # Tipo Tramite de Baja
    TITNUMEROTRAMITEBAJA = Column(String(20))  # Nro Tramite de Baja
    TITMOTIVOBAJA = Column(String(400))  # Movitvo de Baja
    TLQID = Column(Integer)  # Numero de Tipo de Liquidacion
    TITTIPOINTIMACION = Column(String(5))  # Tipo de Intimacion
    ETTID = Column(String(5))  # Campo adicional ETTID
    TITTRACKANDTRACELOTE = Column(String(25))  # Campo adicional TITTRACKANDTRACELOTE
    TITTRACKANDTRACE = Column(String(25))  # Campo adicional TITTRACKANDTRACE
    TITUSUARIONOTIFICACION = Column(String(40))  # Campo adicional TITUSUARIONOTIFICACION
    objeto = relationship("Objeto", back_populates="titulos_deuda")

class EtapasLiquidacion(Base):
    __tablename__ = 'etapas_liquidacion'

    ELNID = Column(Integer, primary_key=True)  # Eln Id
    TITID = Column(Integer, nullable=False)  # Título ID
    ETPID = Column(String(5), nullable=False)  # ID# Etapa
    ELNFECHAINICIO = Column(Date, nullable=False)  # Fecha de Inicio
    ELNFECHAFIN = Column(Date)  # Fecha de Fin
    TBEID = Column(String(7))  # Codigo de Baja de Etapa
    ELNUSUARIOALTA = Column(String(40), nullable=False)  # Usuario de Alta
    ELNFECHAALTA = Column(Date, nullable=False)  # Fecha de Alta
    ELNUSUARIOMODIFICACION = Column(String(40))  # Usuario Modificacion
    ELNFECHAMODIFICACION = Column(Date)  # Fecha de Modificacion
    ELNUSUARIOBAJA = Column(String(40))  # Usuario de Baja
    ELNFECHABAJA = Column(Date)  # Fecha de Baja
    ELNIMPORTEHONORARIOS = Column(Numeric(14, 2))  # eln Importe Honorarios
    ELNCODIGOBARRAS = Column(String(100))  # eln Codigo Barras
    ELNLLNID = Column(Integer)  # eln LLN ID
    ELNMEDICION = Column(Numeric(18, 0))  # eln Medicion

class Etapas(Base):
    __tablename__ = 'etapas'

    ETPID = Column(String(5), primary_key=True)  # ID# Etapa
    ETPDESCRIPCION = Column(String(80), nullable=False)  # Descripcion Etapa
    ETPEMBARGO = Column(String(1), nullable=False)  # Embargo
    ETPREPETITIVA = Column(String(1), nullable=False)  # Repetitiva
    TLQID = Column(Integer)  # ID# Tipo Liquidacion
    ETPFECHAINICIO = Column(Date, nullable=False)  # Fecha de Inicio
    ETPFECHAFIN = Column(Date)  # Fecha Fin
    ETPUSUARIOALTA = Column(String(40), nullable=False)  # Usuario Alta
    ETPFECHAALTA = Column(Date, nullable=False)  # Fecha Alta
    ETPUSUARIOMODIFICACION = Column(String(40))  # Usuario Modificacion
    ETPFECHAMODIFICACION = Column(Date)  # Fecha Modificacion
    ETPUSUARIOBAJA = Column(String(40))  # Usuario Baja
    ETPFECHABAJA = Column(Date)  # Fecha Baja
    ETPSOLOPROCURADOR = Column(String(1), nullable=False)  # Solo Procurador
    ETPCONDONAHONORARIOS = Column(String(1))  # Condona Honorarios
    ETPADMITEIMPORTES = Column(String(1))  # Admite Importes
    ETPANULAGASTOS = Column(String(1))  # Anula Gastos

class DetallesTitulosDeuda(Base):
    __tablename__ = 'detalles_titulos_deuda'

    DTDID = Column(Integer, primary_key=True)  # ID# Detalle Titulo Deuda
    TITID = Column(Integer, nullable=False)  # Título ID
    OBNID = Column(String(30), nullable=False)  # Id Obligacion
    DTDIMPORTE = Column(Numeric(17, 2), nullable=False)  # dtd Importe
    DTDOBSERVACIONES = Column(String(100), nullable=False)  # Observaciones
    DTDFECHAINICIO = Column(Date, nullable=False)  # Fecha de Inicio
    DTDFECHAFIN = Column(Date, nullable=False)  # Fecha de Fin
    DTDUSUARIOALTA = Column(String(40), nullable=False)  # dtd Usuario Alta
    DTDFECHAALTA = Column(Date, nullable=False)  # dtd Fecha Alta
    DTDUSUARIOMODIFICACION = Column(String(40), nullable=False)  # dtd Usuario Modificacion
    DTDFECHAMODIFICACION = Column(Date, nullable=False)  # dtd Fecha Modificacion
    DTDUSUARIOBAJA = Column(String(40), nullable=False)  # dtd Usuario Baja
    DTDFECHABAJA = Column(Date, nullable=False)  # dtd Fecha Baja
    DTDINTERES = Column(Numeric(17, 2), nullable=False)  # dtd Interes
    DTDDIFCUOTA = Column(Integer, nullable=False)  # Diferencia Cuota
    DTDDIFPERIODO = Column(String(6), nullable=False)  # Diferencia Periodo
    DTDDIFORIGEN = Column(String(1), nullable=False)  # Diferencia Origen
    DTDDIFIMPORTE = Column(Numeric(16, 2), nullable=False)  # Diferencia Importe
    BOAID = Column(Integer, nullable=False)  # Boleta
    DTDFECHAVENCIMIENTO = Column(Date, nullable=False)  # Fecha de Vencimiento

Objeto.titulos_deuda = relationship("TituloDeuda", back_populates="objeto")